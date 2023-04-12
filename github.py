"""GIT-распределенная система контроля версий,это система для отслеживание и ведения истории изменения файлов,
в вашем проекте.При помощи распределенности git еще и организовывается командная работа."""


"""репозиторий-это хранилище вашего кода и истории его изменений"""


"""GITHUB-веб-сайт для размещения git-репозиториев в совместной разработке проектов"""


"""Команды GIT":
1. git init-она создает новый локальный репозиторий,
в той директории в которой была прописана команда.(Команда вволится один раз в начале)
2. git add - команда для добавления изменений в систему отслеживания  гита
3.git commit -m '<comment>' - команда для сохранения всех изменений в локальном репозитории с комментарием к ним
4.git remote add <origin> <url> - это команда для того чтобы связать ваш локальный репо с удаленым репо в гитхабе
5. git push <origin> <main> - команда отправки всех ваших изменений на удаленый репо
"""
#___________________________________________________________________________________
"""1)git init
        2)git add .
        3)git commit -m ''
4)git remote add origin <url>
        5)git push origin master"""
#
# daniel@daniel-HP-250-G8-Notebook-PC:~/Рабочий стол/обучение$ git --version
# git version 2.34.1
# daniel@daniel-HP-250-G8-Notebook-PC:~/Рабочий стол/обучение$ git fetch
# fatal: не найден git репозиторий (или один из родительских каталогов): .git
# daniel@daniel-HP-250-G8-Notebook-PC:~/Рабочий стол/обучение$ ls
# builtin_func.py  comprohensions.py  decorators.py  scopes.py  try...except.py  виселица.py  угадайчисло.py  функции.py
# daniel@daniel-HP-250-G8-Notebook-PC:~/Рабочий стол/обучение$ ssh-keygen -o
# Generating public/private rsa key pair.
# Enter file in which to save the key (/home/daniel/.ssh/id_rsa):
# /home/daniel/.ssh/id_rsa already exists.
# Overwrite (y/n)?
# daniel@daniel-HP-250-G8-Notebook-PC:~/Рабочий стол/обучение$
# daniel@daniel-HP-250-G8-Notebook-PC:~/Рабочий стол/обучение$ ls
# builtin_func.py  comprohensions.py  decorators.py  scopes.py  try...except.py  виселица.py  угадайчисло.py  функции.py
# daniel@daniel-HP-250-G8-Notebook-PC:~/Рабочий стол/обучение$ ls -a
# .  ..  builtin_func.py  comprohensions.py  decorators.py  .idea  scopes.py  try...except.py  виселица.py  угадайчисло.py  функции.py
# daniel@daniel-HP-250-G8-Notebook-PC:~/Рабочий стол/обучение$ cd
# daniel@daniel-HP-250-G8-Notebook-PC:~$ ls -a
#  .               .cache       .gnupg      main          .psql_history     snap                        .thunderbird   Изображения     Шаблоны
#  ..              .config      index.png   .mozilla      PycharmProjects   .ssh                        .vscode        Музыка
#  .bash_history   danuiel      .java       new_project   pyproject.toml    .sudo_as_admin_successful   Видео          Общедоступные
#  .bash_logout    .dotnet      .lesshst    .pki          .python_history   sword.png                   Документы      пр.jpeg
#  .bashrc         .gitconfig   .local      .profile      pyton_projects    taskmanager                 Загрузки      'Рабочий стол'
# daniel@daniel-HP-250-G8-Notebook-PC:~$ cat id_rsa.pub
# cat: id_rsa.pub: Нет такого файла или каталога
# daniel@daniel-HP-250-G8-Notebook-PC:~$ cd .ssh
# daniel@daniel-HP-250-G8-Notebook-PC:~/.ssh$ cat id_rsa.pub
# ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABgQDA7LQtjW4/7Uiu3fyGRyjIdhZVSHkbYTbKiUJR2TqFQSzJYlmmwbzGefRcSu+j9RJNI035YD1c6Z89E14jqzWJPPsSpxPtKk1VP1rxA73Zu/GT5bVfNXyuRO8RgV+qsqFuHaeyQm6jWieNiswGhYy9qVxwjYiSudimzYg7t/8IZzT08/KWnfzmwwyqGkRaS0sKUCtQmS4HWN8aScjot1To5SiGFyTO/hsEXoQvTOqXZbeUAb533UrjuImRjxbP3bGXiJiHUIFhnbwc2sukI7ObNWyctTwESZ8z9IfjlTdo/6zFFm55aOY+gZYPILPGrn9rX9NeVQK/i4K8E3k8XofXgqbZL0FMhRBUESZNwll2Wft9UJ2li5OFu4FLTjPhlLnqifbCbDhg7sM8a7zCDYZCpdXbqI+jzj5cOy2py5rW464Iixz3fb2s3R3+UZLYiH/09twX8VEF4Hsc+Uy/hVvBP4IbXygDTryEHPmQOFLKb7Yua6BmkKD0J07WXYuwomM= daniel@daniel-HP-250-G8-Notebook-PC
# daniel@daniel-HP-250-G8-Notebook-PC:~/.ssh$ cd ..
# daniel@daniel-HP-250-G8-Notebook-PC:~$ ls
#  danuiel     main          PycharmProjects   pyton_projects   sword.png     Видео       Загрузки      Музыка          пр.jpeg         Шаблоны
#  index.png   new_project   pyproject.toml    snap             taskmanager   Документы   Изображения   Общедоступные  'Рабочий стол'
# daniel@daniel-HP-250-G8-Notebook-PC:~$ ls 'Рабочий стол'
#  class.py                 Danjdsnf     dictionary.py   py28         задачи.py  'Создать папку'  'Функции строк.py'
#  DanielZhanbolotov.docx   ddaaaaa.py   models.py       website.py   обучение   'Список:).py'
# daniel@daniel-HP-250-G8-Notebook-PC:~$ cd обучение
# bash: cd: обучение: Нет такого файла или каталога
# daniel@daniel-HP-250-G8-Notebook-PC:~$ cd 'обучение'
# bash: cd: обучение: Нет такого файла или каталога
# daniel@daniel-HP-250-G8-Notebook-PC:~$ ls
#  danuiel     main          PycharmProjects   pyton_projects   sword.png     Видео       Загрузки      Музыка          пр.jpeg         Шаблоны
#  index.png   new_project   pyproject.toml    snap             taskmanager   Документы   Изображения   Общедоступные  'Рабочий стол'
# daniel@daniel-HP-250-G8-Notebook-PC:~$ cd 'Рабочий стол'
# daniel@daniel-HP-250-G8-Notebook-PC:~/Рабочий стол$ cd обучение
# daniel@daniel-HP-250-G8-Notebook-PC:~/Рабочий стол/обучение$ ls
# builtin_func.py  comprohensions.py  decorators.py  github.py  scopes.py  try...except.py  виселица.py  угадайчисло.py  функции.py
# daniel@daniel-HP-250-G8-Notebook-PC:~/Рабочий стол/обучение$ git config --global user.name "dsadsadsa2245 "
# daniel@daniel-HP-250-G8-Notebook-PC:~/Рабочий стол/обучение$ git config --global user.email "daniel.zhanbolotov@uwis.edu.kg"
# daniel@daniel-HP-250-G8-Notebook-PC:~/Рабочий стол/обучение$ git config --10
# error: unknown option `10'
# использование: git config [<опции>]
#
# Размещение файла конфигурации
#     --global              использовать глобальный файл конфигурации
#     --system              использовать системный файл конфигурации
#     --local               использовать файл конфигурации репозитория
#     --worktree            use per-worktree config file
#     -f, --file <файл>     использовать указанный файл конфигурации
#     --blob <идент-двоичн-объекта>
#                           прочитать настройки из указанного двоичного объекта
#
# Действие
#     --get                 get value: name [value-pattern]
#     --get-all             get all values: key [value-pattern]
#     --get-regexp          get values for regexp: name-regex [value-pattern]
#     --get-urlmatch        получить значение, специфичное для URL: раздел[.переменная] URL
#     --replace-all         replace all matching variables: name value [value-pattern]
#     --add                 добавить новую переменную: имя значение
#     --unset               remove a variable: name [value-pattern]
#     --unset-all           remove all matches: name [value-pattern]
#     --rename-section      переименовать раздел: старое-имя новое-имя
#     --remove-section      удалить раздел: имя
#     -l, --list            показать весь список
#     --fixed-value         use string equality when comparing values to 'value-pattern'
#     -e, --edit            открыть в редакторе
#     --get-color           найти настроенный цвет: раздел [по-умолчанию]
#     --get-colorbool       проверить, существует ли настроенный цвет: раздел [stdout-есть-tty]
#
# Тип
#     -t, --type <>         value is given this type
#     --bool                значение — это «true» (правда) или «false» (ложь)
#     --int                 значение — это десятичное число
#     --bool-or-int         значение — это --bool или --int
#     --bool-or-str         value is --bool or string
#     --path                значение — это путь (к файлу или каталогу)
#     --expiry-date         значение - это дата окончания срока действия
#
# Другое
#     -z, --null            завершать значения НУЛЕВЫМ байтом
#     --name-only           показывать только имена переменных
#     --includes            учитывать директивы include (включения файлов) при запросе
#     --show-origin         показать источник настройки (файл, стандартный ввод, двоичный объект, командная строка)
#     --show-scope          show scope of config (worktree, local, global, system, command)
#     --default <value>     with --get, use default value when missing entry
#
# daniel@daniel-HP-250-G8-Notebook-PC:~/Рабочий стол/обучение$ git config --list
# user.name=dsadsadsa2245
# user.email=daniel.zhanbolotov@uwis.edu.kg
# init.defaultbranch=master
# daniel@daniel-HP-250-G8-Notebook-PC:~/Рабочий стол/обучение$ cd ~/Desktop
# bash: cd: /home/daniel/Desktop: Нет такого файла или каталога
# daniel@daniel-HP-250-G8-Notebook-PC:~/Рабочий стол/обучение$ cd ~/'Рабочий стол'
# daniel@daniel-HP-250-G8-Notebook-PC:~/Рабочий стол$ mkdir testgit
# daniel@daniel-HP-250-G8-Notebook-PC:~/Рабочий стол$ cd testgit
# daniel@daniel-HP-250-G8-Notebook-PC:~/Рабочий стол/testgit$ ls -a
# .  ..  john.txt
# daniel@daniel-HP-250-G8-Notebook-PC:~/Рабочий стол/testgit$ git init
# Инициализирован пустой репозиторий Git в /home/daniel/Рабочий стол/testgit/.git/
# daniel@daniel-HP-250-G8-Notebook-PC:~/Рабочий стол/testgit$ ls -a
# .  ..  .git  john.txt
# daniel@daniel-HP-250-G8-Notebook-PC:~/Рабочий стол/testgit$ git status
# На ветке master
#
# Еще нет коммитов
#
# Неотслеживаемые файлы:
#   (используйте «git add <файл>…», чтобы добавить в то, что будет включено в коммит)
#         john.txt
#
# ничего не добавлено в коммит, но есть неотслеживаемые файлы (используйте «git add», чтобы отслеживать их)
# daniel@daniel-HP-250-G8-Notebook-PC:~/Рабочий стол/testgit$ git add .
# daniel@daniel-HP-250-G8-Notebook-PC:~/Рабочий стол/testgit$
# daniel@daniel-HP-250-G8-Notebook-PC:~/Рабочий стол/testgit$ git status
# На ветке master
#
# Еще нет коммитов
#
# Изменения, которые будут включены в коммит:
#   (используйте «git rm --cached <файл>…», чтобы убрать из индекса)
#         новый файл:    john.txt
#
# daniel@daniel-HP-250-G8-Notebook-PC:~/Рабочий стол/testgit$ git commit -m 'changed john'
# [master (корневой коммит) 57afe1c] changed john
#  1 file changed, 2 insertions(+)
#  create mode 100644 john.txt
# daniel@daniel-HP-250-G8-Notebook-PC:~/Рабочий стол/testgit$ git status
# На ветке master
# нечего коммитить, нет изменений в рабочем каталоге
# daniel@daniel-HP-250-G8-Notebook-PC:~/Рабочий стол/testgit$ 2+2
# 2+2: команда не найдена
# daniel@daniel-HP-250-G8-Notebook-PC:~/Рабочий стол/testgit$ help
# GNU bash, версия 5.1.16(1)-release (x86_64-pc-linux-gnu)
# Показанные ниже команды определены внутри командного процессора.  Чтобы вывести полный список, введите «help».
# Чтобы вывести справку по функции «name», введите «help name».
# Чтобы вывести справку по командному процессору, введите «info bash».
# Чтобы вывести справку по командам, которые отсутствуют в этом списке, введите «man -k» или «info».
#
# Звёздочка (*) рядом с названием команды означает, что эта команда отключена.
#
#  задание [&]                                                                  history [-c] [-d смещение] [n] или history -anrw [файл] или history -ps а>
#  (( выражение ))                                                              if КОМАНДЫ; then КОМАНДЫ; [ elif КОМАНДЫ; then КОМАНДЫ; ]... [ else КОМАН>
#  . файл [аргументы]                                                           jobs [-lnprs] [задание ...] или jobs -x команда [аргументы]
#  :                                                                            kill [-s назв_сигнала | -n номер_сигнала | -назв_сигнала] ид_процесса | н>
#  [ аргумент... ]                                                              let аргумент [аргумент ...]
#  [[ выражение ]]                                                              local [параметр] имя[=значение] ...
#  alias [-p] [имя[=значение] ... ]                                             logout [n]
#  bg [задание ...]                                                             mapfile [-d разделитель] [-n число] [-O начало] [-s число] [-t] [-u fd] [>
#  bind [-lpvsPSVX] [-m раскладка] [-f файл] [-q имя] [-u name] [-r послед_кл>  popd [-n] [+N | -N]
#  break [n]                                                                    printf [-v переменная] формат [аргументы]
#  builtin [встр_команда [аргумент ...]]                                        pushd [-n] [+N | -N | каталог]
#  caller [выражение]                                                           pwd [-LP]
#  case СЛОВО in [ШАБЛОН [| ШАБЛОН]...) КОМАНДЫ ;;]... esac                     read [-ers] [-a массив] [-d разделитель] [-i текст] [-n число_символов] [>
#  cd [-L|[-P [-e]] [-@]] [каталог]                                             readarray [-d delim] [-n count] [-O origin] [-s count] [-t] [-u fd] [-C c>
#  command [-pVv] команда [аргумент ...]                                        readonly [-aAf] [имя[=значение] ...] или readonly -p
#  compgen [-abcdefgjksuv] [-o option] [-A action] [-G globpat] [-W wordlist]>  return [n]
#  complete [-abcdefgjksuv] [-pr] [-DEI] [-o option] [-A action] [-G globpat]>  select ИМЯ [in СЛОВА ... ;] do КОМАНДЫ; done
#  compopt [-o|+o option] [-DEI] [name ...]                                     set [-abefhkmnptuvxBCHP] [-o параметр] [--] [аргумент ...]
#  continue [n]                                                                 shift [n]
#  coproc [ИМЯ] команда [перенаправления]                                       shopt [-pqsu] [-o] [параметр ...]
#  declare [-aAfFgiIlnrtux] [-p] [name[=value] ...]                             source файл [аргументы]
#  dirs [-clpv] [+N] [-N]                                                       suspend [-f]
#  disown [-h] [-ar] [задание ... | pid ...]                                    test [выражение]
#  echo [-neE] [аргумент ...]                                                   time [-p] конвейер
#  enable [-a] [-dnps] [-f файл] [имя ...]                                      times
#  eval [аргумент ...]                                                          trap [-lp] [[аргумент] сигнал ...]
#  exec [-cl] [-a name] [command [argument ...]] [redirection ...]              true
#  exit [n]                                                                     type [-afptP] имя [имя ...]
#  export [-fn] [имя[=значение ...] или export -p                               typeset [-aAfFgiIlnrtux] [-p] name[=value] ...
#  false                                                                        ulimit [-SHabcdefiklmnpqrstuvxPT] [ограничение]
#  fc [-e редактор] [-lnr] [первая] [последняя] или fc -s [шаблон=замена] [ко>  umask [-p] [-S] [режим]
#  fg [задание]                                                                 unalias [-a] имя [имя ...]
#  for ИМЯ [in СЛОВА... ;] do КОМАНДЫ; done                                     unset [-f] [-v] [-n] [имя ...]
#  for (( выраж1; выраж2; выраж3 )); do КОМАНДЫ; done                           until КОМАНДЫ; do КОМАНДЫ; done
#  function ИМЯ { КОМАНДЫ ; } или ИМЯ () { КОМАНДЫ ; }                          переменные — имена и значения некоторых переменных командного процессора
#  getopts optstring name [arg ...]                                             wait [-fn] [-p var] [id ...]
#  hash [-lr] [-p путь] [-dt] [имя ...]                                         while КОМАНДЫ; do КОМАНДЫ; done
#  help [-dms] [шаблон ...]                                                     { КОМАНДЫ ; }
# daniel@daniel-HP-250-G8-Notebook-PC:~/Рабочий стол/testgit$ git status
# На ветке master
# Изменения, которые не в индексе для коммита:
#   (используйте «git add <файл>…», чтобы добавить файл в индекс)
#   (используйте «git restore <файл>…», чтобы отменить изменения в рабочем каталоге)
#         изменено:      john.txt
#
# нет изменений добавленных для коммита
# (используйте «git add» и/или «git commit -a»)
# daniel@daniel-HP-250-G8-Notebook-PC:~/Рабочий стол/testgit$ git add .
# daniel@daniel-HP-250-G8-Notebook-PC:~/Рабочий стол/testgit$ git commit -m "added print"
# [master f1e4c62] added print
#  1 file changed, 1 insertion(+), 1 deletion(-)
# daniel@daniel-HP-250-G8-Notebook-PC:~/Рабочий стол/testgit$ git status
# На ветке master
# нечего коммитить, нет изменений в рабочем каталоге
# daniel@daniel-HP-250-G8-Notebook-PC:~/Рабочий стол/testgit$
