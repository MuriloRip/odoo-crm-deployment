# Análise de Licenciamento: Odoo vs SuiteCRM

Esta análise foi preparada para o escritório, respondendo às dúvidas sobre compartilhamento de código e segurança de dados.

## 1. Odoo Community (LGPLv3)
O Odoo Community Edition é publicado sob a licença **GNU Lesser General Public License v3 (LGPLv3)**.

### Implicações para o Escritório:
*   **Código Personalizado:** Você **NÃO** é obrigado a compartilhar o código de módulos personalizados que criar para uso interno. A LGPLv3 permite que você desenvolva extensões proprietárias sem precisar abrir o código, desde que não distribua o software para terceiros.
*   **Banco de Dados:** A licença não exige a liberação de acesso ao banco de dados. Seus dados permanecem privados e sob seu controle total.
*   **Modificações no Core:** Se você alterar o código-fonte original do Odoo (o "core"), e distribuir essa versão, aí sim precisaria compartilhar essas alterações. Mas para uso interno e módulos separados, o código é seu.

## 2. SuiteCRM (AGPLv3)
O SuiteCRM utiliza a **GNU Affero General Public License v3 (AGPLv3)**.

### Implicações para o Escritório:
*   **Código Personalizado:** A AGPLv3 é mais rigorosa. Se você hospedar o SuiteCRM em um servidor e permitir que usuários interajam com ele via rede (mesmo funcionários), a licença tecnicamente exige que você disponibilize o código-fonte de qualquer modificação feita no sistema para esses usuários.
*   **Risco de "Copyleft":** Existe um debate jurídico sobre se módulos independentes entram nessa regra, mas a AGPLv3 foi feita justamente para fechar a "brecha da nuvem", obrigando o compartilhamento de código em serviços SaaS/Web.

## Conclusão e Recomendação
Para o cenário do escritório, o **Odoo Community (LGPLv3)** é mais seguro juridicamente se a intenção é manter customizações de processos internos em sigilo, pois a licença é menos "contagiosa" que a AGPLv3 do SuiteCRM.

---
*Documento preparado para fins informativos de implantação técnica.*
