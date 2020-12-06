import unittest

class TestMap(unittest.TestCase):
    def test_use(self):
        """普通にmap"""
        def same(v):
            return v

        v = [0, 1, 2]
        m = map(same, v)
        self.assertEqual(list(m), v)

    def test_lambda(self):
        """mapでlambda"""
        v = [0, 1, 2]
        m = map(lambda _v: _v*2, v)
        self.assertEqual(list(m), [0, 2, 4])

    def test_delay(self):
        """mapの遅延評価チェック"""
        self.count = 0
        def same(v):
            self.count = True
            return v

        v = [0, 1, 2]
        m = map(same, v)

        # まだ値を取得していないので、関数は実行されていない
        self.assertEqual(self.count, 0, "call before use")

        # 評価されたため、カウントアップ
        self.assertEqual(list(m), v)
        self.assertEqual(self.count, 1, "call count missing")

        # 一度評価されると返却は空になり再評価はされない
        # そのため、使い回しを考えるならlistで変換しておくと良い
        self.assertEqual(list(m), [])
        self.assertEqual(self.count, 1, "call second time.")


    def test_multi(self):
        """mapに復数のiteratorを割り当てる"""

        # mapもiteratorなので割り当てられる
        vs = [0, 1, 2, 5, 7, 8]
        ws = [2, 3, 4]
        xs = map(lambda x: x, [6, 9, 3])
        l = list(map(lambda v, w, x: v + w + x, vs, ws, xs))

        self.assertEqual(len(l), 3, "復数のイテレータが与えられた場合、最小の要素数で停止")
        self.assertEqual(l, [8, 13, 9], "結果")

