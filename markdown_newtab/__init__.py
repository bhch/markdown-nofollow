"""
New Tab Extension for Python-Markdown
=====================================

Modify the behavior of Links in Python-Markdown to open a in a new
window. This changes the HTML output to add target="_blank" to all
generated links.
"""

from __future__ import absolute_import
from __future__ import unicode_literals
from markdown import Extension, Markdown
from markdown.inlinepatterns import \
	LinkPattern, ReferencePattern, AutolinkPattern, AutomailPattern, \
	LINK_RE, REFERENCE_RE, SHORT_REF_RE, AUTOLINK_RE, AUTOMAIL_RE

class NewTabMixin(object):
	def handleMatch(self, m):
		el = super(NewTabMixin, self).handleMatch(m)
		if el != None: el.set('target', '_blank')
		return el

class NewTabLinkPattern(     NewTabMixin, LinkPattern):      pass
class NewTabReferencePattern(NewTabMixin, ReferencePattern): pass
class NewTabAutolinkPattern( NewTabMixin, AutolinkPattern):  pass
class NewTabAutomailPattern( NewTabMixin, AutomailPattern):  pass

class NewTabExtension(Extension):
	"""Modifies HTML output to open links in a new tab."""
	def extendMarkdown(self, md, md_globals):
		md.inlinePatterns['link'] = \
			NewTabLinkPattern(LINK_RE, md)
		md.inlinePatterns['reference'] = \
			NewTabReferencePattern(REFERENCE_RE, md)
		md.inlinePatterns['short_reference'] = \
			NewTabReferencePattern(SHORT_REF_RE, md)
		md.inlinePatterns['autolink'] = \
			NewTabAutolinkPattern(AUTOLINK_RE, md)
		md.inlinePatterns['automail'] = \
			NewTabAutomailPattern(AUTOMAIL_RE, md)

def makeExtension(configs = {}):
	return NewTabExtension(configs = configs)
