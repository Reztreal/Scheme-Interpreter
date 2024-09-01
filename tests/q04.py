test = {
  'names': [
    'q04',
    'q4',
    'Q4',
    '4'
  ],
  'points': 2,
  'suites': [
    [
      {
        'locked': True,
        'test': r"""
        >>> global_frame = create_global_frame()
        >>> global_frame.define("x", 3)
        >>> global_frame.parent   # parent of the global frame
        1d6597b6524ad591af6e2f47e176b869
        # locked
        >>> global_frame.lookup("x")
        0c31fd9672da616fabf24f1c95cc313f
        # locked
        >>> global_frame.lookup("foo")
        377055b6dcfd7e506af592ae723fa0cb
        # locked
        # choice: None
        # choice: SchemeError
        # choice: 3
        """,
        'type': 'doctest'
      },
      {
        'locked': True,
        'test': r"""
        >>> first_frame = create_global_frame()
        >>> first_frame.define("x", 3)
        >>> second_frame = Frame(first_frame)
        >>> second_frame.parent
        14587441a61d983705847f2886e98c62
        # locked
        # choice: None
        # choice: first_frame
        # choice: second_frame
        >>> second_frame.lookup("x")
        0c31fd9672da616fabf24f1c95cc313f
        # locked
        """,
        'type': 'doctest'
      }
    ],
    [
      {
        'never_lock': True,
        'test': r"""
        >>> eval("(+ 2 3)")
        5
        >>> eval("(+)")
        0
        >>> eval("(* (+ 3 2) (+ 1 7))")
        40
        >>> eval("(odd? 13)")
        True
        >>> eval("(car (list 1 2 3 4))")
        1
        >>> eval("hello")
        SchemeError
        >>> eval("(car car)")
        SchemeError
        >>> eval("(odd? 1 2 3)")
        SchemeError
        """,
        'type': 'doctest'
      }
    ]
  ]
}