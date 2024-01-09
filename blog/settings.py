# -*- coding: utf-8 -*-

import os
import sys

basedir = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))

prefix = 'sqlite:///'


class BaseConfig(object):
    SECRET_KEY = os.getenv('SECRET_KEY', 'dev key')
    EMAIL = ''
    DEBUG_TB_INTERCEPT_REDIRECTS = False

    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_RECORD_QUERIES = True

    CKEDITOR_ENABLE_CSRF = True
    CKEDITOR_FILE_UPLOADER = 'admin.upload_image'

    POST_PER_PAGE = 10
    MANAGE_POST_PER_PAGE = 15
    COMMENT_PER_PAGE = 15
    # ('theme name', 'display name')
    THEMES = {'perfect_blue': 'Perfect Blue', 'black_swan': 'Black Swan'}
    SLOW_QUERY_THRESHOLD = 1

    UPLOAD_PATH = os.path.join(basedir, 'uploads')
    ALLOWED_IMAGE_EXTENSIONS = ['png', 'jpg', 'jpeg', 'gif']


class ProductionConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI = prefix + 'data.db'
    print(SQLALCHEMY_DATABASE_URI)


config = {
    'production': ProductionConfig
}
