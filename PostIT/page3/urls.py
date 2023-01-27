from unicodedata import name
from django.urls import path
from . import views
# from .views import HomeView

urlpatterns = [
    #     path('', views.home, name='home-page'),
    path('', views.home_timeline, name='home-page'),
    path('', views.home_timeline, name='expanded-post-page'),
    path('upload_reply/<int:pk>',
         views.upload_reply, name='upload_reply'),

    #     path('post/<int:post_id>', views.post_details, name='post-page'),
    path('add_post', views.add_post, name='add-post'),
    path('add_image_post', views.add_image_post, name="add-image-post"),
    path('add_video_post', views.add_video_post, name="add-video-post"),
    path('post/edit/<int:post_id>', views.edit_post, name='edit-post'),
    path('post/edit_images/<int:post_id>',
         views.edit_image_post, name='edit-image-post'),
    path('post/edit_video/<int:post_id>',
         views.edit_video_post, name='edit-video-post'),
    path('post/delete/<int:post_id>', views.delete_post, name='delete-post'),
    path('category/<str:cat>/', views.category, name='posts-by-category'),
    # path('like/', views.like_post, name='like-post'),
    # path('like/<int:pk>', views.like_post_details, name='like-post-details'),
    path('like/', views.like, name='like'),
    path('setLikes/', views.set_likes, name='set_likes'),
    path('updateSession/', views.update_session, name='update_session'),
    path('getSessionData/', views.get_session_data, name='get_session_data'),

    path('fetch_replies_to_reply/', views.fetch_replies_to_reply,
         name='fetch_replies_to_reply'),
    # REST API views
    path('posts', views.post_list_view, name='post-list-view'),
    #     path('', views.home_view, name='home-page'),
    path('getPosts/', views.getPosts, name='get-posts-rest'),
    path('getPosts/<int:pk>', views.getPost, name='get-post-rest'),
    path('getPosts/<int:pk>/update', views.updatePost, name='update-post-rest'),
    path('getPosts/<int:pk>/delete', views.deletePost, name='delete-post-rest'),

    #     Communities section
    path('create_community', views.create_community, name='create-community'),
    path('community/<int:community_id>',
         views.community_page, name='community-page'),
    path('join_community', views.join_community, name='join_community'),
    path('add_post_community/<int:community_id>',
         views.add_post_community, name='add-post-community'),
    path('add_image_post_community/<int:community_id>',
         views.add_image_post_community, name='add-image-post-community'),
    path('add_video_post_community/<int:community_id>',
         views.add_video_post_community, name='add-video-post-community'),


    path('posts/<str:user>', views.posts_by_user, name="posts-by-user"),
    path('create_gamer_profile/<str:user>',
         views.create_game_profile, name="create-gamer-profile"),
    path('matchmaking/<str:user>', views.MatchmakingHome, name="matchmaking-home"),
    path('matchmaking_data/<str:user>',
         views.Matchmaking_Data, name="matchmaking-data"),
    path('getgamerank_server/<str:game>',
         views.get_game_rank_server, name="get-game-rank-server"),
    path('start_following/<str:who_to_follow>',
         views.start_following, name="start-following"),
    path('search', views.search_results, name='search')
]
