from typing import Optional
from fastapi import APIRouter, Response, status, Depends
from enum import Enum

from app.router.blog_post import required_funtionality

router = APIRouter(
    prefix='/blog',
    tags=['blog']
)

# @router.get('/all')
# def get_all_blogs():
#     return {'message': 'All blogs provided'}


@router.get(
    '/all',
    summary='Retrieve all blogs',
    description='This api calls simulates fetching all blogs',
    response_description='The list of available blogs'
)
def get_blogs(page: int = 1, page_size: Optional[int] = None, req_parameter: dict = Depends(required_funtionality)):
    return {'message': f'All {page_size} blogs on page {page}', 'req': req_parameter}


@router.get('/{id}/comments/{comment_id}', tags=['comment'])
def get_comment(id: int, comment_id: int, valid: bool = True, username: Optional[str] = None, req_parameter: dict = Depends(required_funtionality)):
    """
    Simulates retrieving a comment of a blog

    - **id** mandatory path parameter
    - **comment_id** mandatory path parameter
    - **valid** optional query parameter
    - **username** optional query parameter
    """
    return {'message': f'blog_id {id}, comment_id {comment_id}, valid {valid}, username {username}'}


class BlogType(str, Enum):
    short = 'short'
    story = 'story'
    howto = 'howto'


@router.get('/type/{type}')
def get_blog_type(type: BlogType, req_parameter: dict = Depends(required_funtionality)):
    return {'message': f'Blog type {type}'}


@router.get('/{id}', status_code=status.HTTP_200_OK)
def get_blog(id: int, response: Response, req_parameter: dict = Depends(required_funtionality)):
    if id > 5:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {'error': f'Blog {id} not found'}
    else:
        response.status_code = status.HTTP_200_OK
        return {'message': f'Blog with id {id}'}
