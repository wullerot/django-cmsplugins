from __future__ import unicode_literals

import re

from . import conf


class VideoMixin(object):
    _video_url = None
    _video_id = None
    _video_type = None
    _video_domain = None
    _video_attrs = None

    def __init__(self, *args, **kwargs):
        super(VideoMixin, self).__init__(*args, **kwargs)
        self._video_url = getattr(self, 'video_url', None)
        self._video_attrs = kwargs.get('video_attrs', [])
        if self._video_url is None:
            self._video_url = kwargs.get('video_url')
        if self._video_url:
            for rule in conf.VIDEOS_RE_RULES:
                r = re.compile(rule)
                result, matches = r.subn(self.__repl, self._video_url)
                if matches:
                    self._video_id, self._video_type = result.split('__and__')
                    self._video_domain = conf.VIDEOS_DOMAINS[self._video_type]
                    break

    def __repl(self, m):
        repl = m.groupdict()
        result = ''
        if repl.has_key('youtube_id'):
            result = repl['youtube_id'] + '__and__' + 'youtube'
        elif repl.has_key('vimeo_id'):
            result = repl['vimeo_id'] + '__and__' + 'vimeo'
        return result

    @property
    def video_id(self):
        return self._video_id

    @property
    def video_type(self):
        return self._video_type

    @property
    def video_embed_url(self):
        url = None
        attrs = self.get_video_attrs()
        if self._video_type == 'youtube':
            url = '{0}embed/{1}'.format(self._video_domain, self._video_id)
        elif self._video_type == 'vimeo':
            url = '{0}video/{1}'.format(self._video_domain, self._video_id)
        if attrs:
            url = '{0}?{1}'.format(url, attrs)
        return url

    @property
    def video_jsapi_url(self):
        url = None
        attrs = self.get_video_attrs()
        if self._video_type == 'youtube':
            url = '{0}watch?v={1}{1}'.format(self._video_domain,
                                             self._video_id)
        elif self._video_type == 'vimeo':
            attrs = '?api=1&player_id=vimeoplayer'
            url = '{0}video/{1}{2}'.format(self._video_domain, self._video_id,
                                           attrs)
        return url

    def get_video_attrs(self):
        return '&'.join(self._video_attrs)
