def results(fields, original_query):
  _, command, _ = original_query.split(' ')
  id = fields['~id']
  user, repo = id.split('/')
  html = open("js.html").read().replace("{USER}", user).replace("{REPO}", repo)
  return {
    "title": "Flashpm '{0}'".format(id),
    "run_args": [command, user, repo],
    "html": html
  }

def run(command, user, repo):
    from subprocess import Popen
    if command == 'install':
      Popen(['./shell/install.sh', 'https://github.com/{0}/{1}/archive/master.zip'.format(user, repo), repo])
    elif command == 'remove':
      Popen(['./shell/remove.sh', repo])

if __name__=='__main__':
  run("remove", "mmarcon/flashlight-test-plugin")
