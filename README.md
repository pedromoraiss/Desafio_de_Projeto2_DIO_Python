# Desafio: Criando um sistema bancário v2

## Objetivo geral

Separar as funções existentes de saque, depósito e extrato em funções. Criar duas novas funções: cadastrar usuário (cliente) e cadastrar conta bancária.

## Instruções

### 1.Função depósito

A função depósito deve receber os argumentos apenas por posição (positional only). Sugestão de argumentos: saldo, valor, extrato. Sugestão de retorno: saldo e extrato.   

### 2. Função Saque

A função saque deve receber os argumentos apenas por nome (keyword only). Sugestão de argumentos: saldo, valor, extrao, limite, numero_saques, limite_saques. Sugestão de retorno: saldo e extrato.

### 3.Função extrato

A função deve receber os argumentos por posição e nome (positional only e keyword only). Argumentos posicionais: saldo, argumentos nomeados: extrato.

## Novas funções

### Função criar usuário

O programa deve armazenar os usuários em uma lista, um usuário é composto por: nome, data de nascimento, cpf e endereço. Deve ser armazenado somente os números do CPF. Não podemos cadastrar 2 usuários com o mesmo CPF.

### Função Criar conta

O programa deve armazenar contas em uma lista, uma conta é composta por: âgencia, número da conta e usuário. O número da conta é sequencial, iniciando em 1. O número da agência é fixo: "0001". O usuário pode ter mais de uma conta, mas uma conta pertence a somente um usuário.

## Contribua

Este é um desafio de projeto feito por mim com o conhecimento que estou adquirindo ao longo do bootcamp "Potência Tech powered by iFood | Ciência de Dados com Python!". Caso queira contribuir ou deixar algum feedback de como posso ta melhorando meu código sinta-se livre!


