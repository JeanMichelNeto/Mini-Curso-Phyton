TEXT
Quando terminar de responder as perguntas acima, faça este exercício.

Scenario 1: Crie uma outra conta na AWS, acessando sua conta principal no menu My Organization, através da segunda opção Create account.
Scenario 2: Agora, crie uma outra conta usando a opção Invite account. Para isso, você precisar criar essa conta antes.
No total do dia, você precisa ter 3 contas criadas na AWS, na seguinte estrutura:

Organizaçõa das contas:

Master Account/Payer Account
    1 OU: Dev
      Dev Account
    1 OU: Prod
      Prod Account
      
Na conta de Dev, os usuarios não devem conseguir criar RDS
Na conta de Prod, os usuarios não devem conseguir criar S3

Simule o uso dessas SCP em cada conta, usando outros browsers para poder logar
em multiplas contas ao mesmotempo.
Ex.: Chrome para logar na Master Account, Firefox para logar na conta Dev com o Root(email da conta) e 
Modo incongnito do firefox ou do Chrome para logar na conta de Prod com o Root(email da conta).

Obs: Use SCP para definir essas regra, e attach em cada conta sua respectiva SCP.
Execute o exercicio, grave um video da sua tela e envie o resultado no grupo do Telegram, me marque lá(Mateus Prado)
Imagina que você quer que alguem pegue esse material e consiga fazer sozinho, como se você estivesse fazendo um tutorial, how-to para a comunidade! Como você gostaria que fosse esse material? Pense como se fosse você procurando isso no Google :)

Troque informações no grupo do Telegram, tire dúvidas, compartilhe idéias com os colegas do grupo.

Boa sorte

Mateus