Feature: codebreaker submits guess

  The codebreaker submits a guess of four numbers. The game marks the guess with + and - signs.

  For each number ....

  Scenario Outline: submit guess
    Given the secret code "<code>"
    When I guess "<guess>"
    Then the mark should be "<mark>"

    Scenarios: no matches
      | code | guess | mark |
      | 1234 | 5555  |      |

    Scenarios: one number correct
      | code | guess | mark |
      | 1234 | 1555  | +    |
      | 1234 | 2555  | -    |

    Scenarios: two numbers correct
      | code | guess | mark |
      | 1234 | 1255  | ++   |
      | 1234 | 1355  | +-   |
      | 1234 | 2355  | --   |

    Scenarios: three numbers correct
      | code | guess | mark |
      | 1234 | 1235  | +++- |
      | 1234 | 1245  | ++-  |
      | 1234 | 1425  | +--  |
      | 1234 | 4325  | ---  |

    Scenarios: all numbers correct
      | code | guess | mark |
      | 1234 | 1234  | ++++ |
      | 1234 | 1243  | ++-- |
      | 1234 | 1423  | +--- |
      | 1234 | 4321  | ---- |