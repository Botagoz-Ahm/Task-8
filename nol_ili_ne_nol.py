from itertools import repeat
print(
    0 in list(
        map(
            lambda x:
            int(
                x()
                ),
            repeat(
                input,
                int(
                    input()
                    )
                )
            )
        )
    )
