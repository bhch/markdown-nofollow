# markdown-nofollow

This extension modifies the HTML output of Python-Markdown to add `rel="nofollow"` attribute to all links.

# Usage

  >>> import markdown
  >>> from md_nofollow import NofollowExtension
  
  >>> raw_text = "Lets add nofollow to [links](http://github.com)"
  >>> markdown.markdown(raw_text, extensions=[NofollowExtension()]
  "<p>Lets add nofollow to <a href="http://github.com" rel="nofollow">links</a></p>"
  

# Credits

This is a fork of [markdown-newtab](https://github.com/Undeterminant/markdown-newtab) which adds `target="_blank"` to links. The code has been modifed to add `rel="nofollow"`. 
