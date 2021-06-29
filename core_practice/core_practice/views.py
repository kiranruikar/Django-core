from django.http import HttpResponse, HttpResponseRedirect


# def home(request):
# 	# print(request)
# 		# <WSGIRequest: GET '/abc/'>

# 	# print(dir(request))
# 		#['COOKIES', 'FILES', 'GET', 'META', 'POST', '__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_current_scheme_host', '_encoding', '_get_full_path', '_get_post', '_get_raw_host', '_get_scheme', '_initialize_handlers', '_load_post_and_files', '_mark_post_parse_error', '_messages', '_read_started', '_set_post', '_stream', '_upload_handlers', 'body', 'build_absolute_uri', 'close', 'content_params', 'content_type', 'csrf_processing_done', 'encoding', 'environ', 'get_full_path', 'get_full_path_info', 'get_host', 'get_port', 'get_raw_uri', 'get_signed_cookie', 'headers', 'is_ajax', 'is_secure', 'method', 'parse_file_upload', 'path', 'path_info', 'read', 'readline', 'readlines', 'resolver_match', 'scheme', 'session', 'upload_handlers', 'user', 'xreadlines']

# 	# print(request.method)
# 		# GET

# 	# print(request.path)
# 		#/abc/

# 	# print(request.headers)
# 		#{'Content-Length': '', 'Content-Type': 'text/plain', 'Host': '127.0.0.1:8000', 'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:89.0) Gecko/20100101 Firefox/89.0', 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8', 'Accept-Language': 'en-US,en;q=0.5', 'Accept-Encoding': 'gzip, deflate', 'Connection': 'keep-alive', 'Cookie': 'csrftoken=5yYKr9tot1Lk5sBVarHin9iik3Ha3lUjND4ItmC7YCjxkwJ4Cl6R6PqeUlP8VdXz; sessionid=caor93uz294d8u7yyh2sx0qn26sjcelr', 'Upgrade-Insecure-Requests': '1', 'Cache-Control': 'max-age=0'}

# 	# print(request.get_full_path())
# 	# print(request.environ)
# 		#{'SHELL': '/bin/bash', 'SESSION_MANAGER': 'local/Casper:@/tmp/.ICE-unix/1653,unix/Casper:/tmp/.ICE-unix/1653', 'QT_ACCESSIBILITY': '1', 'COLORTERM': 'truecolor', 'XDG_CONFIG_DIRS': '/etc/xdg/xdg-ubuntu:/etc/xdg', 'XDG_MENU_PREFIX': 'gnome-', 'GNOME_DESKTOP_SESSION_ID': 'this-is-deprecated', 'LANGUAGE': 'en_IN:en', 'GNOME_SHELL_SESSION_MODE': 'ubuntu', 'SSH_AUTH_SOCK': '/run/user/1000/keyring/ssh', 'XMODIFIERS': '@im=ibus', 'DESKTOP_SESSION': 'ubuntu', 'SSH_AGENT_PID': '1612', 'GTK_MODULES': 'gail:atk-bridge', 'DBUS_STARTER_BUS_TYPE': 'session', 'PWD': '/media/kiran/80F2D810F2D80BF21/DJango/DJango Practice/Django Core/core_practice', 'LOGNAME': 'kiran', 'XDG_SESSION_DESKTOP': 'ubuntu', 'XDG_SESSION_TYPE': 'x11', 'GPG_AGENT_INFO': '/run/user/1000/gnupg/S.gpg-agent:0:1', 'XAUTHORITY': '/run/user/1000/gdm/Xauthority', 'WINDOWPATH': '2', 'HOME': '/home/kiran', 'USERNAME': 'kiran', 'IM_CONFIG_PHASE': '1', 'LANG': 'en_IN', 'LS_COLORS': 'rs=0:di=01;34:ln=01;36:mh=00:pi=40;33:so=01;35:do=01;35:bd=40;33;01:cd=40;33;01:or=40;31;01:mi=00:su=37;41:sg=30;43:ca=30;41:tw=30;42:ow=34;42:st=37;44:ex=01;32:*.tar=01;31:*.tgz=01;31:*.arc=01;31:*.arj=01;31:*.taz=01;31:*.lha=01;31:*.lz4=01;31:*.lzh=01;31:*.lzma=01;31:*.tlz=01;31:*.txz=01;31:*.tzo=01;31:*.t7z=01;31:*.zip=01;31:*.z=01;31:*.dz=01;31:*.gz=01;31:*.lrz=01;31:*.lz=01;31:*.lzo=01;31:*.xz=01;31:*.zst=01;31:*.tzst=01;31:*.bz2=01;31:*.bz=01;31:*.tbz=01;31:*.tbz2=01;31:*.tz=01;31:*.deb=01;31:*.rpm=01;31:*.jar=01;31:*.war=01;31:*.ear=01;31:*.sar=01;31:*.rar=01;31:*.alz=01;31:*.ace=01;31:*.zoo=01;31:*.cpio=01;31:*.7z=01;31:*.rz=01;31:*.cab=01;31:*.wim=01;31:*.swm=01;31:*.dwm=01;31:*.esd=01;31:*.jpg=01;35:*.jpeg=01;35:*.mjpg=01;35:*.mjpeg=01;35:*.gif=01;35:*.bmp=01;35:*.pbm=01;35:*.pgm=01;35:*.ppm=01;35:*.tga=01;35:*.xbm=01;35:*.xpm=01;35:*.tif=01;35:*.tiff=01;35:*.png=01;35:*.svg=01;35:*.svgz=01;35:*.mng=01;35:*.pcx=01;35:*.mov=01;35:*.mpg=01;35:*.mpeg=01;35:*.m2v=01;35:*.mkv=01;35:*.webm=01;35:*.ogm=01;35:*.mp4=01;35:*.m4v=01;35:*.mp4v=01;35:*.vob=01;35:*.qt=01;35:*.nuv=01;35:*.wmv=01;35:*.asf=01;35:*.rm=01;35:*.rmvb=01;35:*.flc=01;35:*.avi=01;35:*.fli=01;35:*.flv=01;35:*.gl=01;35:*.dl=01;35:*.xcf=01;35:*.xwd=01;35:*.yuv=01;35:*.cgm=01;35:*.emf=01;35:*.ogv=01;35:*.ogx=01;35:*.aac=00;36:*.au=00;36:*.flac=00;36:*.m4a=00;36:*.mid=00;36:*.midi=00;36:*.mka=00;36:*.mp3=00;36:*.mpc=00;36:*.ogg=00;36:*.ra=00;36:*.wav=00;36:*.oga=00;36:*.opus=00;36:*.spx=00;36:*.xspf=00;36:', 'XDG_CURRENT_DESKTOP': 'ubuntu:GNOME', 'VTE_VERSION': '6003', 'GNOME_TERMINAL_SCREEN': '/org/gnome/Terminal/screen/c88fe207_d596_4771_98e8_1bffe414bf82', 'INVOCATION_ID': '7fcc231e065a4cd7b49a05ce11dcc83b', 'MANAGERPID': '1425', 'LESSCLOSE': '/usr/bin/lesspipe %s %s', 'XDG_SESSION_CLASS': 'user', 'TERM': 'xterm-256color', 'LESSOPEN': '| /usr/bin/lesspipe %s', 'USER': 'kiran', 'GNOME_TERMINAL_SERVICE': ':1.114', 'DISPLAY': ':0', 'SHLVL': '1', 'QT_IM_MODULE': 'ibus', 'DBUS_STARTER_ADDRESS': 'unix:path=/run/user/1000/bus,guid=f4ee926db5d1f99e86fc628660d2e7b5', 'XDG_RUNTIME_DIR': '/run/user/1000', 'JOURNAL_STREAM': '8:42282', 'XDG_DATA_DIRS': '/usr/share/ubuntu:/usr/local/share/:/usr/share/:/var/lib/snapd/desktop', 'PATH': '/home/kiran/.local/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin', 'GDMSESSION': 'ubuntu', 'DBUS_SESSION_BUS_ADDRESS': 'unix:path=/run/user/1000/bus,guid=f4ee926db5d1f99e86fc628660d2e7b5', '_': '/usr/bin/python3', 'OLDPWD': '/media/kiran/80F2D810F2D80BF21/DJango/DJango Practice/Django Core', 'DJANGO_SETTINGS_MODULE': 'core_practice.settings', 'TZ': 'UTC', 'RUN_MAIN': 'true', 'SERVER_NAME': 'localhost', 'GATEWAY_INTERFACE': 'CGI/1.1', 'SERVER_PORT': '8000', 'REMOTE_HOST': '', 'CONTENT_LENGTH': '', 'SCRIPT_NAME': '', 'SERVER_PROTOCOL': 'HTTP/1.1', 'SERVER_SOFTWARE': 'WSGIServer/0.2', 'REQUEST_METHOD': 'GET', 'PATH_INFO': '/abc/', 'QUERY_STRING': '', 'REMOTE_ADDR': '127.0.0.1', 'CONTENT_TYPE': 'text/plain', 'HTTP_HOST': '127.0.0.1:8000', 'HTTP_USER_AGENT': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:89.0) Gecko/20100101 Firefox/89.0', 'HTTP_ACCEPT': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8', 'HTTP_ACCEPT_LANGUAGE': 'en-US,en;q=0.5', 'HTTP_ACCEPT_ENCODING': 'gzip, deflate', 'HTTP_CONNECTION': 'keep-alive', 'HTTP_COOKIE': 'csrftoken=5yYKr9tot1Lk5sBVarHin9iik3Ha3lUjND4ItmC7YCjxkwJ4Cl6R6PqeUlP8VdXz; sessionid=caor93uz294d8u7yyh2sx0qn26sjcelr', 'HTTP_UPGRADE_INSECURE_REQUESTS': '1', 'HTTP_CACHE_CONTROL': 'max-age=0', 'wsgi.input': <django.core.handlers.wsgi.LimitedStream object at 0x7f0435a5bf70>, 'wsgi.errors': <_io.TextIOWrapper name='<stderr>' mode='w' encoding='utf-8'>, 'wsgi.version': (1, 0), 'wsgi.run_once': False, 'wsgi.url_scheme': 'http', 'wsgi.multithread': True, 'wsgi.multiprocess': False, 'wsgi.file_wrapper': <class 'wsgiref.util.FileWrapper'>, 'CSRF_COOKIE': '5yYKr9tot1Lk5sBVarHin9iik3Ha3lUjND4ItmC7YCjxkwJ4Cl6R6PqeUlP8VdXz'}

# 	# print(request.get_host)
# 		#<bound method HttpRequest.get_host of <WSGIRequest: GET '/abc/'>>

# 	# print(request.get_port)
# 		#<bound method HttpRequest.get_port of <WSGIRequest: GET '/abc/'>>

# 	# print(request.path_info)
# 		#/abc/

# 	# print(request.scheme)
# 		# HTTP
# 	# print(request.user)
# 	# print(request.upload_handlers)
# 	# print(request.xreadlines)
# 	# print(request.is_ajax)
# 		#<bound method HttpRequest.is_ajax of <WSGIRequest: GET '/abc/'>>

# 	# print(request.is_secure)
# 		#<bound method HttpRequest.is_secure of <WSGIRequest: GET '/abc/'>>

# 	return HttpResponse("<!DOCTYPE html><html><head><style>h1 {color: red}</style></head><body><h1>hello world</h1></body></html>") 


def home(request):
    response = HttpResponse()
    response.content = "<!DOCTYPE html><html><head><style>h1 {color: red}</style></head><body><h1>hello world</h1></body></html>"
    response.content = "Some new lines"
    response.write("<p>Page not found</p>")
    print(response.status_code)
    return response


def redirect_somewhere(request):
    return HttpResponseRedirect("/some/path")
