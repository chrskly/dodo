dodo
====

dodo is very simple online todo list. It displays a list of tasks with the oldest first so that hopfully you won't let them sit there too long.

It's written in Python and uses Django.

To run:

    python manage.py runserver 0.0.0.0:8080

Here's an NGinx conf snippet which will proxy through the requests and do auth for you as well.

    server {
        server_name my.awesome.server.com;
        location / {
            auth_basic "Restricted";
            auth_basic_user_file htpasswd;
            proxy_pass_header Server;
            proxy_set_header Host $http_host;
            proxy_redirect off;
            proxy_set_header X-Real-IP $remote_addr;
            proxy_set_header X-Scheme $scheme;
            proxy_connect_timeout 600;
            proxy_read_timeout 600;
            proxy_pass http://localhost:8080/;
        }
    }
