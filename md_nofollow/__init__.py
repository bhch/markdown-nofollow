"""
Nofollow Extension for Python-Markdown
=====================================

Modify the behavior of Links in Python-Markdown by adding rel="nofollow"
to all generated links.
"""

from __future__ import absolute_import
from __future__ import unicode_literals
from markdown import Extension, Markdown
from markdown.inlinepatterns import \
	LinkPattern, ReferencePattern, AutolinkPattern, AutomailPattern, \
	LINK_RE, REFERENCE_RE, SHORT_REF_RE, AUTOLINK_RE, AUTOMAIL_RE

class NofollowMixin(object):
	def handleMatch(self, m):
		el = super(NofollowMixin, self).handleMatch(m)
		if el != None: el.set('rel', 'nofollow')
		return el

class NofollowLinkPattern(     NofollowMixin, LinkPattern):      pass
class NofollowReferencePattern(NofollowMixin, ReferencePattern): pass
class NofollowAutolinkPattern( NofollowMixin, AutolinkPattern):  pass
class NofollowAutomailPattern( NofollowMixin, AutomailPattern):  pass

class NofollowExtension(Extension):
	"""Modifies HTML output to open links in a new tab."""
	def extendMarkdown(self, md, md_globals):
		md.inlinePatterns['link'] = \
			NofollowLinkPattern(LINK_RE, md)
		md.inlinePatterns['reference'] = \
			NofollowReferencePattern(REFERENCE_RE, md)
		md.inlinePatterns['short_reference'] = \
			NofollowReferencePattern(SHORT_REF_RE, md)
		md.inlinePatterns['autolink'] = \
			NofollowAutolinkPattern(AUTOLINK_RE, md)
		md.inlinePatterns['automail'] = \
			NofollowAutomailPattern(AUTOMAIL_RE, md)

def makeExtension(configs = {}):
	return NofollowExtension(configs = configs)
