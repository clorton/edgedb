##
# Copyright (c) 2010 Sprymix Inc.
# All rights reserved.
#
# See LICENSE for details.
##


from semantix.caos.backends import pool


class ConnectionPool(pool.ConnectionPool):
    def __init__(self, connector, backend):
        super().__init__()
        self.connector = connector
        self.backend = backend

    def create(self):
        c = self.connector(pool=self)
        c.connect()
        return c

    def recycle(self, connection):
        super().recycle(connection)
        connection.reset()
