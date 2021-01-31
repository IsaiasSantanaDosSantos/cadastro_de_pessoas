
from time import sleep

print('~' * 20)
print('\033[0:36mCADASTRO DE CLIENTES\033[m')
print('~' * 20)
i = 0
while i != 2:
    i = int(input('Vamos iniciar seu cadastro? \nEscolha uma opção:\n[ 1 ] Para \033[0:36mSIM\033[m  \n[ 2 ] Para \033[0:36mNÃO\033[m\nOpção: '))
    if i == 1:
        print('Vamos lá!...')
        sleep(0.3)
        op = 0
        while op != 3:
            print('''
Escolha uma opção:
[ 1 ] Para \033[0:31mPESSOA FISICA\033[m
[ 2 ] Para \033[0:31mPESSOA JURIDICA\033[m
[ 3 ] Para \033[0:31mVOLTAR\033[m''')
            op = int(input('Qual a opção? '))
            print('~' * 20)
            if op == 1:
                print('Iniciando cadastro pessoa \033[0:31mFISICA\033[m...')
                sleep(0.5)
                nomeFisico = str(input('Digite seu nome completo: ')).strip().title()
                tel = str(input('Digite seu telefone com DDD: ')).lstrip().strip()
                cpf = str(input('Digite o número de seu CPF: '))
                lagradouro = str(input('Digite o lagradouro: ')).strip().title()
                cep = str(input('Digite seu cep: ')).strip()
                bairro = str(input('Digite o bairro: ')).title().strip()
                municipio = str(input('Digite o município: ')).strip().title()
                estado = str(input('Digite o estado: ')).strip().title()
                print('~' * 20)
                print('\033[0:31mCONFIRA SEUS DADOS\033[m')
                print('~' * 20)
                print(nomeFisico)
                print(tel)
                print(cpf)
                print(lagradouro)
                print(cep)
                print(bairro)
                print(municipio)
                print(estado)
                print('~' * 20)
                conf = 0
                while conf != 2:
                    print('Seus dados estão corretos? ')
                    conf = print('''
Escolha uma opção:
[ 1 ] Para \033[0:36mSIM\033[m
[ 2 ] Para \033[0:36mCORRIGIR\033[m''')
                    conf = int(input('Digite sua opção: '))
                    if conf == 1:
                        print('Dados salvo com sucesso!!')
                        sleep(0.6)
                        break
                    elif conf == 2:
                        print('Voltando para refaze-los...')
                        sleep(0.6)
                    else:
                        print('Não tem a opção {} no MENU, tente novamente.'.format(conf))
                        sleep(0.6)

            elif op == 2:
                print('Iniciando cadastro pessoa \033[0:36mJURIDICA\033[m...')
                sleep(0.5)
                razãoSocioal = str(input('Digite o nome da razão social: ')).strip().upper()
                nomeFantasia = str(input('Digite o nome fantasia: ')).strip().title()
                cnpj = str(input('Digite o CNPJ: ')).strip()
                tel = str(input('Digite seu telefone com DDD: ')).lstrip().strip()
                lagradouro = str(input('Digite o lagradouro: ')).strip().title()
                cep = str(input('Digite seu cep: ')).strip()
                bairro = str(input('Digite o bairro: ')).title().strip()
                municipio = str(input('Digite o município: ')).strip().title()
                estado = str(input('Digite o estado: ')).strip().title()
                print('~' * 20)
                print('\033[0:31mCONFIRA SEUS DADOS\033[m')
                print('~' * 20)
                print(razãoSocioal)
                print(nomeFantasia)
                print(cnpj)
                print(tel)
                print(lagradouro)
                print(cep)
                print(bairro)
                print(municipio)
                print(estado)
                print('~' * 20)
                corr = 0
                while corr != 2:
                    print('Seus dados estão corretos? ')
                    conf = int(input('''
Escolha uma opção:
[ 1 ] Para \033[0:36mSIM\033[m
[ 2 ] Para \033[0:36mCORRIGIR\033[m'''))
                    if corr == 1:
                        print('Dados salvo com sucesso!!')
                    elif corr == 2:
                        print('Voltando para refaze-los...')
                        sleep(0.6)
                    else:
                        print('Digito inválido! Tente novamente.')
                        sleep(0.6)

            elif op == 3:
                print('Voltando...')
                sleep(0.7)

            else:
                print('Não tem a opção {} no MENU. Tente novamente.'.format(op))

    elif i == 2:
        print('OK! Saindo...')
        sleep(0.5)
        print('Finalizando programa...')
        sleep(1)
        print('Obrigado!')

    else:
        print('Não tem a opção {} no MENU. Tente novamente.'.format(i))

print('O \033[0:31mprogramador Isaias\033[m agradece a sua participação!\nVolte sempre.')
sleep(1)
print('Bye, bye...')
sleep(1)
print('Bye...')
