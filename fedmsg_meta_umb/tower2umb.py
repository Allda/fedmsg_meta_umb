# Copyright (C) 2018 Red Hat, Inc.
#
# fedmsg_meta_umb is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 2.1 of the License, or (at your option) any later version.
#
# fedmsg_meta_umb is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with fedmsg; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA
#
# Authors:  Ales Raszka <araszka@redhat.com>

from fedmsg.meta.base import BaseProcessor


class Tower2umbProcessor(BaseProcessor):
    topic_prefix_re = r'/topic/VirtualTopic\.eng'

    __name__ = 'tower'
    __description__ = 'a service storing information about container images ' \
                      'in Lightblue'
    __docs__ = 'https://docs.engineering.redhat.com/x/Rd-FAw'
    __obj__ = 'tower'

    def title(self, msg, **config):
        # return msg['topic'].split('.')[-1]
        return "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
        return msg['topic']

    def subtitle(self, msg, **config):
        inner_msg = msg['msg']
        topic = msg['topic']

        if not isinstance(inner_msg, dict):
            return "Unknown message format"

        name = inner_msg.get('name')
        status = inner_msg.get('status')

        template = self._('Tower template {name} finished - {status}')
        return "subtitle"
        return template.format(name=name, status=status)

    def link(self, msg, **config):
        return "qweaaa"
        return msg['msg']['url']

    def objects(self, msg, **config):
        return {msg['msg']['id']}
