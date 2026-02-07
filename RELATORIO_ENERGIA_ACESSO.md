# Relatório: Consumo de Energia e Acesso Remoto (Escritório vs. Casa)

Este relatório analisa a viabilidade técnica de manter o servidor Odoo e o ngrok ativos no escritório, abordando o consumo elétrico e as formas de gerenciamento remoto.

## 1. Consumo de Energia em Modo de Suspensão

O modo de suspensão (**Sleep Mode**) é extremamente eficiente em termos energéticos. Neste estado, o computador desliga quase todos os componentes (processador, discos rígidos, ventoinhas), mantendo apenas a memória RAM energizada para que o sistema retorne instantaneamente de onde parou.

| Estado do PC | Consumo Estimado (Watts) | Custo Estimado (Mensal/24h) |
| :--- | :--- | :--- |
| **Ligado (Idle/Ocioso)** | 30W - 60W | R$ 15,00 - R$ 30,00 |
| **Suspenso (Sleep)** | 1W - 5W | R$ 0,50 - R$ 2,50 |
| **Desligado (Mas na tomada)** | 0.5W - 1W | < R$ 0,50 |

> **Conclusão:** O gasto de energia em modo de suspensão é insignificante (equivalente a uma pequena lâmpada LED). No entanto, o **ngrok não funciona** enquanto o PC está suspenso, pois o processador e a placa de rede param de processar dados.

## 2. O Problema do ngrok em Suspensão

O ngrok depende de uma conexão ativa com a internet e processamento contínuo para manter o túnel aberto.
*   **Em Suspensão:** O túnel cai imediatamente. Ao "acordar" o PC, o ngrok pode tentar reconectar, mas o endereço (URL) pode mudar se você não usar um domínio estático (pago).
*   **Recomendação:** Se o Odoo precisa estar disponível 24h, o PC **não pode suspender**. Para economizar, você pode configurar o monitor para desligar após 1 minuto, o que economiza a maior parte da energia visível.

## 3. Modificando de Casa para o Escritório

Sim, você pode gerenciar tudo de casa. Existem três formas principais de fazer isso com segurança:

### Opção A: Chrome Remote Desktop (Mais Fácil)
*   **O que é:** Uma extensão do Google Chrome que permite ver e controlar a tela do PC do escritório.
*   **Vantagem:** Gratuito, funciona através de firewalls e é muito fácil de instalar.
*   **Uso:** Você abre o navegador em casa e vê a área de trabalho do escritório como se estivesse lá.

### Opção B: Tailscale (Mais Profissional/Seguro)
*   **O que é:** Uma VPN de "configuração zero". Ele cria uma rede privada entre seu PC de casa e o do escritório.
*   **Vantagem:** Você pode acessar o Odoo pelo IP interno (ex: `http://100.x.x.x:8069`) sem precisar do ngrok e sem expor nada para a internet pública.
*   **Uso:** Ideal para quem quer segurança máxima e não quer depender de links públicos do ngrok.

### Opção C: Wake-on-LAN (Acordar Remotamente)
*   **O que é:** Uma tecnologia que permite ligar o PC do escritório enviando um "pacote mágico" pela rede.
*   **Requisito:** Precisa de configuração na BIOS e no roteador do escritório.
*   **Uso:** Você deixa o PC desligado e "acorda" ele apenas quando precisar trabalhar.

## 4. Recomendações Finais

1.  **Para Uso Constante:** Deixe o PC ligado, mas configure para **desligar apenas o monitor**. O consumo de um PC moderno em repouso (sem monitor) é baixo.
2.  **Para Gerenciamento:** Instale o **Chrome Remote Desktop** no PC do escritório. Assim, de casa, você pode abrir o terminal, usar o `nano` e rodar o script `update_odoo.sh` que criamos.
3.  **Para o ngrok:** Se o link cair, você acessa via Chrome Remote Desktop e reinicia o terminal.

---
**Referências:**
1. [Consumo de Energia de Computadores - TechTudo](https://www.techtudo.com.br/guia/2024/08/quanto-um-pc-gasta-de-energia-saiba-calcular-e-como-economizar-edinfoeletro.ghtml)
2. [Documentação Oficial ngrok - Agent Reconnect](https://ngrok.com/docs/agent)
3. [Tailscale - How it works](https://tailscale.com/blog/how-tailscale-works/)
