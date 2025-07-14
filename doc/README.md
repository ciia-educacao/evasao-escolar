# Organização das pastas no diretório `/doc`

- `include/` → Arquivos utilizados pelo Pandoc para transformar documentos Markdown (MD) em PDF ou outros formatos.

# Exemplos de comandos para geração de documentos em outros formatos

Para gerar um PDF a partir de um arquivo Markdown (`input.md`) usando o Pandoc com as configurações do arquivo `defaults.yaml`, você pode usar o seguinte comando:

```sh
pandoc --defaults include/defaults.yaml "input.md" --lua-filter include/diagram.lua --filter pandoc-include
```
