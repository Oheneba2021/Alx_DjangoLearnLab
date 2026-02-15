from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile, Post, Comment, Tag


class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]

    def clean_email(self):
        email = self.cleaned_data.get("email")
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("This email is already in use.")
        return email


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ["username", "email"]


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ["bio", "profile_picture"]

class PostForm(forms.ModelForm):
    tags = forms.CharField(
        required=False,
        help_text="Comma-separated tags (e.g. django, python, web)",
    )

    class Meta:
        model = Post
        fields = ["title", "content", "tags"]

    def clean_title(self):
        title = (self.cleaned_data.get("title") or "").strip()
        if len(title) < 3:
            raise forms.ValidationError("Title must be at least 3 characters long.")
        return title

    def clean_tags(self):
        raw = (self.cleaned_data.get("tags") or "").strip()
        if not raw:
            return []
        # normalize: split by comma, trim, lowercase
        tags = [t.strip().lower() for t in raw.split(",") if t.strip()]
        # remove duplicates while preserving order
        seen = set()
        unique = []
        for t in tags:
            if t not in seen:
                seen.add(t)
                unique.append(t)
        return unique

    def save(self, commit=True):
        post = super().save(commit=commit)
        tag_names = self.cleaned_data.get("tags", [])

        if commit:
            post.tags.clear()
            for name in tag_names:
                tag_obj, _ = Tag.objects.get_or_create(name=name)
                post.tags.add(tag_obj)

        return post

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["content"]

    def clean_content(self):
        content = (self.cleaned_data.get("content") or "").strip()
        if len(content) < 2:
            raise forms.ValidationError("Comment is too short.")
        return content