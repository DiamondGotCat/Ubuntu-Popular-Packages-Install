import subprocess

def install_packages():
    # Update the package list
    subprocess.run(['sudo', 'apt', 'update'], check=True)
    
    # Install the basic packages
    basic_packages = [
        '7-zip', 'abiword', 'audacity', 'blender', 'chromium', 'codeblocks', 'eclipse', 
        'filezilla', 'gimp', 'geany', 'inkscape', 'kdenlive', 'libreoffice', 'meld', 
        'mozilla-thunderbird', 'netbeans-ide', 'notepad++', 'openshot', 'pidgin', 'ruby', 
        'python3.6', 'sublime-text3', 'thunderbird', 'vim', 'visual-studio-code'
    ]
    subprocess.run(['sudo', 'apt', 'install', '-y'] + basic_packages, check=True)
    
    # Install the developer tools packages
    developer_tools = [
        'clang-format', 'cmake', 'doxygen', 'flex', 'git', 'gradle', 'g++', 'gnupg', 
        'gtk+-3.0', 'libc6-dev', 'libgtk2.0-dev', 'libncurses5-dev', 'libreadline-dev', 
        'libuv1-dev', 'libwebkitgtk-1.0-dev', 'nodejs', 'npm', 'python3.6', 'ruby'
    ]
    subprocess.run(['sudo', 'apt', 'install', '-y'] + developer_tools, check=True)
    
    # Install the programming languages packages
    programming_languages = [
        'python3.6', 'ruby', 'nodejs', 'java', 'javascript', 'go', 'c++', 'csharp', 
        'rust', 'swift', 'php', 'perl', 'lua', 'haskell', 'scheme', 'lisp', 'tcl', 
        'ruby-on-rails', 'django', 'flask', 'pyramid', 'cherrypy', 'turbogears', 'web.py', 
        'bottle', 'falcon', 'pyspark', 'pysparkling', 'scikit-learn', 'tensorflow', 'keras', 
        'pytorch', 'chainer', 'caffe', 'opencv', 'scikit-image'
    ]
    subprocess.run(['sudo', 'apt', 'install', '-y'] + programming_languages, check=True)
    
    # Install the networking packages
    networking_packages = [
        'firefox-addons', 'google-chrome', 'thunderbird'
    ]
    subprocess.run(['sudo', 'apt', 'install', '-y'] + networking_packages, check=True)
    
    # Install the office packages
    office_packages = [
        'libreoffice', 'openoffice'
    ]
    subprocess.run(['sudo', 'apt', 'install', '-y'] + office_packages, check=True)
    
    # Install the text editors packages
    text_editors = [
        'gimp', 'inkscape', 'kate', 'libreoffice', 'notepad++', 'sublime-text3', 'vim', 'visual-studio-code'
    ]
    subprocess.run(['sudo', 'apt', 'install', '-y'] + text_editors, check=True)
    
    # Install the web development packages
    web_development_packages = [
        'chrome-web-store', 'firefox-addons', 'google-chrome', 'mozilla-thunderbird'
    ]
    subprocess.run(['sudo', 'apt', 'install', '-y'] + web_development_packages, check=True)

if __name__ == "__main__":
    install_packages()
