import sublime, sublime_plugin, http.client, urllib, json

API_KEY  = ''
HOSTNAME = ''
PROJECT  = ''

class RedminePasteCommand(sublime_plugin.TextCommand):
  def run(self, view):
    syntax = self.view.settings().get('syntax')
    lang = syntax.split('/')[1]
    for region in self.view.sel():
      if not region.empty():
        content = self.view.substr(region)
      else:
        content = self.view.substr(sublime.Region(0, self.view.size()))
    
    r, p = http.client.HTTPSConnection(HOSTNAME), urllib.parse.urlencode({'paste_title': '', 'paste[text]': content, 'paste[lang]': lang, 'paste_submit' : 1})
    h = {"Content-type": "application/x-www-form-urlencoded",
         "X-Redmine-API-Key": API_KEY,
         "Accept": "text/plain"}
    r.request("POST", "/projects/" + PROJECT + "/pastes.json", p, h)
    g = r.getresponse()
    if g.status == 302:
        url = g.getheader('Location')
        sublime.set_clipboard(url)
        sublime.status_message('Link has been copied to your clipboard - ' + url)
    else:
      sublime.status_message('Failure: ' + g.reason)
    r.close()
