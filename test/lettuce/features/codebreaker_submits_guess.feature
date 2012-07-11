Feature: codebreaker submits guess

  The codebreaker submits a guess of four numbers. The game marks the guess with + and - signs.

  For each number ....

  Scenario Outline: submit guess
    Given the secret code "<code>"
    When I guess "<guess>"
    Then the mark should be "<mark>"

    Examples:
      | code | guess | mark |
      | 1234 | 5555  |      |

    Examples:
      | code | guess | mark |
      | 1234 | 1555  | +    |
      | 1234 | 2555  | -    |

    Examples:
      | code | guess | mark |
      | 1234 | 1255  | ++   |
      | 1234 | 3255  | +-   |
      | 1234 | 2355  | --   |

    Examples:
      | code | guess | mark |
      | 1234 | 1235  | +++  |
      | 1234 | 4235  | ++-  |
      | 1234 | 1425  | +--  |
      | 1234 | 4325  | ---  |

    Examples:
      | code | guess | mark |
      | 1234 | 1234  | ++++ |
      | 1234 | 1243  | ++-- |
      | 1234 | 1423  | +--- |
      | 1234 | 4321  | ---- |

    Examples:
      | code | guess | mark |
      | 1234 | 1155  | +    |
      | 1234 | 5115  | -    |
      | 1134 | 1155  | ++   |
      | 1134 | 5115  | +-   |
      | 1134 | 5511  | --   |
      | 1134 | 1115  | ++   |
      | 1134 | 5111  | +-   |