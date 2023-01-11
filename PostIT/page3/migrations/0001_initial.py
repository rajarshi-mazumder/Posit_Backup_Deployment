# Generated by Django 3.2.15 on 2023-01-11 06:56

from django.conf import settings
import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('tags', models.CharField(default='none', max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Community',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('bio', models.TextField(blank=True, null=True)),
                ('profile_pic', models.ImageField(blank=True, null=True, upload_to='images/profile')),
                ('community_header_pic', models.ImageField(blank=True, null=True, upload_to='images/profile')),
                ('is_private', models.BooleanField(blank=True, default=False, null=True)),
                ('post_date', models.DateField(auto_now_add=True, null=True)),
                ('post_datetime', models.DateTimeField(auto_now_add=True, null=True)),
                ('rules', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, default='', max_length=500, null=True), blank=True, default=list, null=True, size=None)),
                ('community_admins', models.ManyToManyField(blank=True, default=None, related_name='community_admins', to=settings.AUTH_USER_MODEL)),
                ('created_by', models.ForeignKey(default=None, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
                ('members', models.ManyToManyField(blank=True, default=None, related_name='members', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='GameProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('age', models.IntegerField(blank=True, default=None, null=True)),
                ('game', models.CharField(choices=[('Valorant', 'Valorant'), ('Call of Duty', 'Call of Duty'), ('League of Legends', 'League of Legends'), ('Counter Strike: GO', 'Counter Strike: GO')], max_length=50)),
                ('region', models.CharField(choices=[('Val', [('APAC', 'APAC'), ('EMEA', 'EMEA'), ('NA', 'NA'), ('LATAM', 'LATAM')]), ('COD', [('APAC', 'APAC'), ('EMEA', 'EMEA'), ('NA', 'NA')]), ('LOL', [('APAC', 'APAC'), ('EMEA', 'EMEA'), ('NA', 'NA')]), ('CS', [('APAC', 'APAC'), ('EMEA', 'EMEA'), ('NA', 'NA'), ('LATAM', 'LATAM')])], max_length=50, null=True)),
                ('servers', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, default='', max_length=50, null=True), blank=True, default=list, null=True, size=None)),
                ('rank', models.CharField(choices=[('Val', [('IRON', 'Iron'), ('Bronze', 'Bronze'), ('Silver', 'Silver'), ('Gold', 'Gold'), ('Platinum', 'Platinum '), ('Diamond', 'Diamond'), ('Asencdant', 'Asencdant'), ('Immortal', 'Immortal'), ('Radiant', 'Radiant')]), ('COD', [('Rookie', 'Rookie'), ('Veteran', 'Veteran'), ('Elite', 'Elite'), ('Pro', 'Pro'), ('Master', 'Master'), ('Grandmaster', 'Grandmaster'), ('Legendary', 'Legendary')]), ('LOL', [('IRON', 'Iron'), ('Bronze', 'Bronze'), ('Silver', 'Silver'), ('Gold', 'Gold'), ('Platinum', 'Platinum '), ('Diamond', 'Diamond'), ('Master', 'Master'), ('Grandmaster', 'Grandmaster'), ('Challenger', 'Challenger')]), ('CS', [('Silver', 'Silver'), ('Gold', 'Gold'), ('Master Guardian', 'Master Guardian'), ('Distinguished Master Guardian', 'Distinguished Master Guardian'), ('Legendary', 'Legendary'), ('Elite', 'Elite')])], default='', max_length=50)),
                ('peak_rank', models.CharField(default='', max_length=50, null=True)),
                ('user_status', models.CharField(choices=[('Looking for teams', 'Looking for teams'), ('Looking for talent', 'Looking for talent'), ('none', 'none')], default='none', max_length=50)),
                ('in_game_user_id', models.CharField(blank=True, default='', max_length=400, null=True)),
                ('years_of_exp', models.IntegerField(blank=True, default=0)),
                ('roles_rating', django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(default=0, null=True), blank=True, default=list, null=True, size=None)),
                ('achievements', models.CharField(blank=True, default='', max_length=400)),
                ('experience', django.contrib.postgres.fields.ArrayField(base_field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=300, null=True), blank=True, default=list, null=True, size=None), blank=True, default=list, null=True, size=None)),
                ('looking_for_friends', models.BooleanField(default=False)),
                ('time_available', models.CharField(blank=True, max_length=300, null=True)),
                ('communication_level', models.IntegerField(blank=True, default=0, null=True)),
                ('additional_info', django.contrib.postgres.fields.ArrayField(base_field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, default='', max_length=500, null=True), blank=True, default=list, null=True, size=None), blank=True, default=list, null=True, size=None)),
                ('remarks', models.CharField(blank=True, default='', max_length=400, null=True)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=255, null=True)),
                ('reply_to', models.IntegerField(blank=True, default=-1, null=True)),
                ('is_reply', models.BooleanField(blank=True, default=False, null=True)),
                ('is_parent_a_reply', models.BooleanField(blank=True, default=False, null=True)),
                ('reply_root', models.IntegerField(blank=True, default=-1, null=True)),
                ('post_date', models.DateField(auto_now_add=True, null=True)),
                ('post_datetime', models.DateTimeField(auto_now_add=True, null=True)),
                ('category', models.CharField(default='none', max_length=50, null=True)),
                ('tags', models.CharField(blank=True, default='', max_length=255)),
                ('like_count', models.BigIntegerField(default='0')),
                ('reply_count', models.BigIntegerField(default='0')),
                ('video', models.FileField(blank=True, null=True, upload_to='videos/')),
                ('has_images', models.BooleanField(blank=True, default=False, null=True)),
                ('has_video', models.BooleanField(blank=True, default=False, null=True)),
                ('body', models.CharField(blank=True, max_length=280, null=True)),
                ('images_ids_list', django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(blank=True, default=-1, null=True), blank=True, default=list, null=True, size=None)),
                ('images_urls_list', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, default='', max_length=500, null=True), blank=True, default=list, null=True, size=None)),
                ('is_lft_lfp_post', models.BooleanField(blank=True, default=False, null=True)),
                ('vouch_count', models.BigIntegerField(default='0')),
                ('author', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('community', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='page3.community')),
                ('likes', models.ManyToManyField(blank=True, default=None, related_name='posts', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Tags',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag_name', models.CharField(max_length=50, null=True)),
                ('post', models.ManyToManyField(blank=True, default=None, related_name='tagged_posts', to='page3.Post')),
            ],
        ),
        migrations.CreateModel(
            name='Replies',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reply_to', models.IntegerField(blank=True, default=-1, null=True)),
                ('post_id', models.IntegerField(blank=True, default=-1, null=True)),
                ('reply_root', models.IntegerField(blank=True, default=-1, null=True)),
                ('reply_to_post', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='page3.post')),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bio', models.TextField(blank=True, null=True)),
                ('profile_pic', models.ImageField(blank=True, null=True, upload_to='images/profile')),
                ('discord_link', models.CharField(blank=True, max_length=255, null=True)),
                ('twitch_link', models.CharField(blank=True, max_length=255, null=True)),
                ('is_private', models.BooleanField(blank=True, default=False, null=True)),
                ('age', models.IntegerField(blank=True, default=None, null=True)),
                ('gender', models.CharField(blank=True, choices=[('Male', 'Male'), ('Female', 'Female'), ('Transgender', 'Transgender'), ('Other', 'Other')], default=None, max_length=255, null=True)),
                ('communities', models.ManyToManyField(blank=True, default=None, related_name='communities', to='page3.Community')),
                ('featured_communities', models.ManyToManyField(blank=True, default=None, related_name='featuredCommunities', to='page3.Community')),
                ('followers', models.ManyToManyField(blank=True, default=None, related_name='followers', to=settings.AUTH_USER_MODEL)),
                ('following', models.ManyToManyField(blank=True, default=None, related_name='following', to=settings.AUTH_USER_MODEL)),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('vouched_by', models.ManyToManyField(blank=True, default=None, related_name='vouched_by', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='post',
            name='user_profile',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='page3.profile'),
        ),
        migrations.AddField(
            model_name='post',
            name='vouches',
            field=models.ManyToManyField(blank=True, default=None, related_name='vouches', to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='Main_Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('main_gamer_profile', models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, to='page3.gameprofile')),
                ('user', models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ImageFiles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.FileField(blank=True, null=True, upload_to='images/')),
                ('post', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='page3.post')),
            ],
        ),
    ]
