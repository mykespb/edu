#!/usr/bin/env python

# Mikhail (myke) Kolodin, 2024
# 2025-01-04 2025-01-04 1.0
# ~ packer.py

# ~ Простой сжиматель "упаковщик" текстов ASCII. И распаковщик.
# ~ Если буква встречается 3..255 раз подряд, она заменяется на
# ~ (код + 128), (число повторов (на 1 меньше реального)).
# ~ а. упаковщик
# ~ б. распаковщик
# ~ в. оценка эффективности упаковки и запускальщик

def packer(text: str) -> bytearray:
    """упаковщик"""

    out = bytearray()
    txt = bytearray(text, 'ascii')
    
    cnt = 0
    char = b''
    
    for newc in txt:

        if newc == char:
            cnt += 1

            if cnt == 256:
                out.append(128 | newc)
                out.append(255)
                char = ''
                cnt = 0
            
        else:
            if char:
                if cnt >= 3:
                    out.append(128 | newc)
                    out.append(cnt-1)
                    char = ''
                    cnt = 0
                else:
                    for i in range(cnt):
                        out.append(127 & char)
                    char = newc
                    cnt = 1

            else:
                char = newc
                cnt = 1

    if cnt:
        for i in range(cnt):
            out.append(127 & char)

    return out


def unpacker(text: bytearray) -> str:
    """распаковщик"""

    out = ""
    state = 'out'
    char = ""

    for e in text:
        if e > 127:
            char = e & 127
            state = 'in'
        else:
            if state == 'in':
                for i in range(int(e)+1):
                    out += str(char)
            else:
                out += str(char)

    return out


def tester(sample: str) -> None:
    """только запускаем, печатаем результаты туда-сюда
    и считаем эффективность в процентах
    """

    print("sample to pack:\n", sample, "\nbytes-length=", len(sample))
    packed = packer(sample)
    print(packed, "\nbytes-length=", len(packed), "pack-coef=", len(sample) / len(packed))
    unpacked = unpacker(packed)
    print("unpacked sample:\n", sample, "\nstr-length=", len(unpacked))


samples = [
r"""
    ___   _____ ______________     ___    ____  ______
   /   | / ___// ____/  _/  _/    /   |  / __ \/_  __/
  / /| | \__ \/ /    / / / /     / /| | / /_/ / / /   
 / ___ |___/ / /____/ /_/ /     / ___ |/ _, _/ / /    
/_/  |_/____/\____/___/___/    /_/  |_/_/ |_| /_/
""",
r"""
                         MMMMMMM                     MMMMMMMMMMMMMM
                      MMMMMMMMMMMM                MMMMMMMMMMMMMMMMMMM
                    MMMMMMMMMMMMMMMM                MMMMMMMMMMMMMMMMM
               MMMMMMMMMMMMMMMMMMMMMM              MMMMMMMMMMMMM   MM
            MMMMMMMMMMMMMMMMMMMMMMMMMMM            MMMMMMMMMMM
          MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM        MMMMMMMMMMMM
        MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM    MMMMMMMMMMMMM
        MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
       MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
       MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
       MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
      MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
     MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
    MMMMMMMM  MMMMMMMM  MMMMMMMMMMMMMMMMMMMM
   MMMMM  M   MMMMMMM       MNMMMMMMMMMMMMMM
 MMMMM  MMMM  MMMMMM          MMMMM  MMMMMM
MMMMMM  MMM  MMMMMM           MMMMM   MMMMM
MMMMM     M  MMMMM            MMMM     MMMM
MMMM        MMMMM           MMMMMM      MMMMM
 MMM       MMMMMMM          NMMMMM      MMMMM
 MM         MMMM             MMMM         MMM
MMMM         MMMM           MMMM           MM
 MMM          MMM           MMM            MMM
 MMMM         MMMM         MMM              MMM
 MMMMM         MMM        MMMM               MMM
   MMMMMM      MMMM        MMMM              MMMMMM
      MMM       MMMMM       MMMM              MMMMMM
                  MASTEL                        MMMMM
                    MMMMM
""",
r"""
                   YAao,
                    Y8888b,
                  ,oA8888888b,
            ,aaad8888888888888888bo,
         ,d888888888888888888888888888b,
       ,888888888888888888888888888888888b,
      d8888888888888888888888888888888888888,
     d888888888888888888888888888888888888888b
    d888888P'                    `Y888888888888,
    88888P'                    Ybaaaa8888888888l
   a8888'                      `Y8888P' `V888888
 d8888888a                                `Y8888
AY/'' `\Y8b                                 ``Y8b
Y'      `YP                                    ~~
         `'
""",
r"""
       .-~~``~~-,
      (          \
   .--'`-.__,     \
  /      |\O/      |
 |,      /         |
 \   ,--`\         |
  `.(   /          \
       /            \
      / .  ;    :.   \
     /__;   \   | \   \
     /   '. |\_ /-.'-._\
    |      `   `        \
    |    /               \
    |    |                |
    |    |                \
    \    \                 |
     \    |  |   |   \     \
      \   \  \   \    \     |
       '.  \  \  ' \   \     \
         \  \  `\   `\  `\    \
          |  `\  `\   `.  '.   \
           \   `-. '._  '-. '._/\
            |     \-._;-._ '-._  \
            \      `\     `--` `--\
             ;_      `-.           |
~==~==jgs==~,-.-.-'`;'=~=-.,_   __/=~=~=~~=
  =_ = -_ -( ( ( .-`( ( ( .-``"`-_ = - _ -
- -   =   - ` ` ` _= ` ` `   =  -  -    =
~~==~=~~==~=~~=~~=~=~==~~=~~==~~=~~=~~~===~~
                         \ . \  . '|
                          \   . .' /
                           '.   \.'|
                             '-.__/
""",
r"""
              *         *      *         *
          ***          **********          ***
       *****           **********           *****
     *******           **********           *******
   **********         ************         **********
  ****************************************************
 ******************************************************
********************************************************
********************************************************
********************************************************
 ******************************************************
  ********      ************************      ********
   *******       *     *********      *       *******
     ******             *******              ******
       *****             *****              *****
          ***             ***              ***
            **             *              **
"""
]


def main():
    """запуск"""

    sepa = "\n\n" + 80 * "=" + "\n\n"

    for sample in samples:
        print(sepa)
        tester(sample)
        
    print(sepa)


main()
