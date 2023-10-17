from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, Group, Permission
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils.translation import gettext_lazy as _
from board.managers import UserManager


class Student(AbstractBaseUser, PermissionsMixin):
    name = models.CharField(max_length=100, verbose_name=_('ФИО'))
    username = models.CharField(_('username'), max_length=255, unique=True)
    email = models.EmailField(_('email address'), null=True, blank=True)
    phone = models.CharField(
        _('phone number'), max_length=30, null=True, blank=True)
    student_id = models.IntegerField(verbose_name=_('Студенческий ID'))
    grade = models.PositiveIntegerField(
        verbose_name=_('Оценка'),
        validators=[
            MinValueValidator(0, _("Оценка не может быть меньше 0")),
            MaxValueValidator(100, _("Оценка не может быть больше 100"))
        ]
    )
    is_active = models.BooleanField(_('active'), default=False)
    is_staff = models.BooleanField(_('staff'), default=False)
    is_verified = models.BooleanField(_('verified'), default=False)

    # Добавьте related_name для groups и user_permissions
    groups = models.ManyToManyField(
        Group,
        verbose_name=_('Groups'),
        blank=True,
        help_text=_('The groups this student belongs to.'),
        related_name='students',
        related_query_name='student'
    )
    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name=_('User permissions'),
        blank=True,
        help_text=_('Specific permissions for this student.'),
        related_name='students',
        related_query_name='student'
    )

    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')
        unique_together = ('username', 'email', 'phone')

    def __str__(self):
        return self.name
