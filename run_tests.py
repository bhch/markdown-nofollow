from markdown import Markdown
from unittest import TestCase, main
from markdown_newtab import NewTabExtension

class TestNewTab(TestCase):
	def setUp(self):
		self.md = Markdown(extensions = [NewTabExtension()])
		self.maxDiff = None

	def assertEqualMarkdown(self, before, after):
		self.assertEqual(self.md.convert(before), after)

	def test_link(self):
		self.assertEqualMarkdown("""\
[one](https://ddg.gg) \
[two](https://duck.co "test")""", """\
<p><a href="https://ddg.gg" target="_blank">one</a> \
<a href="https://duck.co" target="_blank" title="test">two</a></p>""")

	def test_reference(self):
		self.assertEqualMarkdown("""\
[one][un] \
[two][deux]

[un]: https://ddg.gg
[deux]: https://duck.co "test\"""", """\
<p><a href="https://ddg.gg" target="_blank">one</a> \
<a href="https://duck.co" target="_blank" title="test">two</a></p>""")

	def test_short_reference(self):
		self.assertEqualMarkdown("""\
[one], \
[two]

[one]: https://ddg.gg
[two]: https://duck.co "test\"""", """\
<p><a href="https://ddg.gg" target="_blank">one</a>, \
<a href="https://duck.co" target="_blank" title="test">two</a></p>""")

	def test_autolink(self):
		self.assertEqualMarkdown("""\
<https://ddg.gg>""", """\
<p><a href="https://ddg.gg" target="_blank">https://ddg.gg</a></p>""")

	def test_automail(self):
		self.assertEqualMarkdown("""\
<address@example.com>""", """\
<p><a href="&#109;&#97;&#105;&#108;&#116;&#111;&#58;&#97;&#100;&#100;\
&#114;&#101;&#115;&#115;&#64;&#101;&#120;&#97;&#109;&#112;&#108;&#101;\
&#46;&#99;&#111;&#109;" target="_blank">&#97;&#100;&#100;&#114;&#101;\
&#115;&#115;&#64;&#101;&#120;&#97;&#109;&#112;&#108;&#101;&#46;&#99;\
&#111;&#109;</a></p>""")

if __name__ == '__main__':
	main()
