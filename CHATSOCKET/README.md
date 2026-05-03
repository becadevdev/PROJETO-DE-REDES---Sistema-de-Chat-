# ChatSocket

Projeto de chat simples usando sockets em Python.

## Arquivos

- `servidor.py` - servidor do chat.
- `cliente.py` - cliente que se conecta ao servidor.

## Requisitos

- Python 3 instalado.

## Como usar

1. Abra um terminal na pasta `CHATSOCKET`.
2. Execute o servidor:

```bash
python servidor.py
```

3. Em outro terminal, execute o cliente:

```bash
python cliente.py
```

4. Digite a mensagem no cliente e ela será enviada ao servidor.

## Git

Para salvar suas mudanças no Git:

```bash
git add .
git commit -m "Atualiza projeto ChatSocket"
git push
```

Se ainda não tiver configurado o remoto:

```bash
git remote add origin <url-do-repositório>
git push -u origin main
```

## Observações

- Se o servidor e o cliente estiverem na mesma máquina, use `localhost`.
- O projeto pode ser usado para estudar como funciona comunicação por sockets em Python.
