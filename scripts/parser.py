from modules import prompt_parser, shared

class Parser:
    def prompt_to_tags(prompt):
        use_prompt_parser = shared.opts.use_prompt_parser_when_save_prompt_to_eagle_as_tags

        p = prompt
        if use_prompt_parser:
            p = ','.join(map(lambda x: x[0].strip(), prompt_parser.parse_prompt_attention(p)))

        return [ x.strip() for x in p.split(",") if x.strip() != "" ]
