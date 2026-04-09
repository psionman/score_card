list:
    just --list

run arg1="" arg2=""  arg3 = "":
    uv run -m score_card.main {{arg1}} {{arg2}} {{arg3}}

test arg1="":
    uv run -m pytest {{arg1}}
