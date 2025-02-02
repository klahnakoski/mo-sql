from unittest import TestCase

from mo_json import STRING, NUMBER

from mo_sql.utils import untyped_column


class TestBasic(TestCase):

    def test_untyped_column(self):
        self.assertEqual(untyped_column("a"), ("a", None))
        self.assertEqual(untyped_column("a.b"), ("a.b", None))
        self.assertEqual(untyped_column("a.$S"), ("a", STRING))
        self.assertEqual(untyped_column("a.b.$S"), ("a.b", STRING))
        self.assertEqual(untyped_column("a.$A.b"), ("a.b", None))
        self.assertEqual(untyped_column("a.$A.b.$N"), ("a.b", NUMBER))
