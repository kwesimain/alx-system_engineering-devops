# Install Nginx package
package { 'nginx':
  ensure => installed,
}

# Create index.html with 'Hello World' content
file { '/var/www/html/index.html':
  content => 'Hello World!',
}

# Create 404 error page with 'Ceci n'est pas une page' content
file { '/var/www/html/xyz.html':
  content => 'Ceci n\'est pas une page',
}

# Create Nginx server block
file { '/etc/nginx/sites-available/default':
  content => "server {
    listen 80 default_server;
    listen [::]:80 default_server;
    root /var/www/html;
    index index.html;

    location /redirect_me {
      return 301 https://en.wikipedia.org/wiki/Nginx;
    }

    error_page 404 /xyz.html;
    location /xyz {
      root /var/www/html;
      internal;
    }
  }",
}

# Enable server block (Symbolic Link)
file { '/etc/nginx/sites-enabled/default':
  ensure => 'link',
  target => '/etc/nginx/sites-available/default',
}

# Restart Nginx service
service { 'nginx':
  ensure => running,
  enable => true,
  require => File['/etc/nginx/sites-enabled/default'],
}

