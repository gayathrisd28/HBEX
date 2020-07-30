"""Functions to parse a file containing student data."""


def all_houses(filename):
    """Return a set of all house names in the given file.

    For example:
      >>> unique_houses('cohort_data.txt')
      {"Dumbledore's Army", 'Gryffindor', ..., 'Slytherin'}

    Arguments:
      - filename (str): the path to a data file

    Return:
      - set[str]: a set of strings
    """

    houses = set()

    cohort_data = open(filename)

    for line in cohort_data:
        house = line.rstrip().split('|')[2]
        if house:
            houses.add(house)

    return houses


def students_by_cohort(filename, cohort='All'):
  students = []
  program_file = open(filename)
  for line in program_file:
    name = line.rstrip().split('|')[0][1]
    cohort_name = line.rstrip().split('|')[-1]

    if cohort_name == cohort:
      students = students.append(name)
    elif cohort_name == 'All':
      students = students.append(name)
    elif cohort == " ":
      students = students.append(name)
   
    # TODO: replace this with your code
    # open the file
    # split the file lines
    # identify indices: index 4 is cohort, index 1 and 2 is name
    
    # if cohort parameter not given, return all student names
    # if cohort does not exist, return empty list
    

  return sorted(students)

def all_names_by_house(filename):
    """Return a list that contains rosters for all houses, ghosts, instructors.

    Rosters appear in this order:
    - Dumbledore's Army
    - Gryffindor
    - Hufflepuff
    - Ravenclaw
    - Slytherin
    - Ghosts
    - Instructors

    Each roster is a list of names sorted in alphabetical order.

    For example:
      >>> rosters = hogwarts_by_house('cohort_data.txt')
      >>> len(rosters)
      7

      >>> rosters[0]
      ['Alicia Spinnet', ..., 'Theodore Nott']
      >>> rosters[-1]
      ['Filius Flitwick', ..., 'Severus Snape']

    Arguments:
      - filename (str): the path to a data file

    Return:
      - list[list]: a list of lists
    """

    dumbledores_army = []
    gryffindor = []
    hufflepuff = []
    ravenclaw = []
    slytherin = []
    ghosts = []
    instructors = []

    # TODO: replace this with your code
    program_file = open(filename)
    first_name = line.rstrip().split('|')[0]
    last_name = line.rstrip().split('|')[1]
    name = f'{first_name} {last_name}'
    house = line.rstrip().split('|')[2]
    cohort_name = line.rstrip().split('|')[-1]
    if house:
        if house == "Dumbledore's Army":
          dumbledores_army = dumbledores_army.append(name)
        elif house == "Gryffindor":
          gryffindor = gryffindor.append(name)
        elif house == "Hufflepuff":
          hufflepuff = hufflepuff.append(name)
        elif house == "Ravenclaw":
          ravenclaw = ravenclaw.append(name)
        elif house == "Slytherin":
          slytherin = slytherin.append(name)
    else:
      if cohort_name == "I":
        instructors = instructors.append(name)
      elif cohort_name == "G":
        ghosts = ghosts.append()
            
    return  [sorted[dumbledores_army, gryffindor, hufflepuff, slytherin, ravenclaw, instructors, ghosts]


def all_data(filename):
    """Return all the data in a file.

    Each line in the file is a tuple of (full_name, house, advisor, cohort)

    Iterate over the data to create a big list of tuples that individually
    hold all the data for each person. (full_name, house, advisor, cohort)

    For example:
      >>> all_student_data('cohort_data.txt')
      [('Harry Potter', 'Gryffindor', 'McGonagall', 'Fall 2015'), ..., ]

    Arguments:
      - filename (str): the path to a data file

    Return:
      - list[tuple]: a list of tuples
    """

    all_data = []

    # TODO: replace this with your code

    return all_data


def get_cohort_for(filename, name):
    """Given someone's name, return the cohort they belong to.

    Return None if the person doesn't exist. For example:
      >>> get_cohort_for('cohort_data.txt', 'Harry Potter')
      'Fall 2015'

      >>> get_cohort_for('cohort_data.txt', 'Hannah Abbott')
      'Winter 2016'

      >>> get_cohort_for('cohort_data.txt', 'Balloonicorn')
      None

    Arguments:
      - filename (str): the path to a data file
      - name (str): a person's full name

    Return:
      - str: the person's cohort or None
    """

    # TODO: replace this with your code


def find_duped_last_names(filename):
    """Return a set of duplicated last names that exist in the data.

    For example:
      >>> find_name_duplicates('cohort_data.txt')
      {'Creevey', 'Weasley', 'Patil'}

    Arguments:
      - filename (str): the path to a data file

    Return:
      - set[str]: a set of strings
    """

    # TODO: replace this with your code


def get_housemates_for(filename, name):
    """Return a set of housemates for the given student.

    Given a student's name, return a list of their housemates. Housemates are
    students who belong to the same house and were in the same cohort as the
    given student.

    For example:
    >>> get_housemates_for('cohort_data.txt', 'Hermione Granger')
    {'Angelina Johnson', ..., 'Seamus Finnigan'}
    """

    # TODO: replace this with your code


##############################################################################
# END OF MAIN EXERCISE.  Yay!  You did it! You Rock!
#

if __name__ == '__main__':
    import doctest

    result = doctest.testfile('doctests.py',
                              report=False,
                              optionflags=(
                                  doctest.REPORT_ONLY_FIRST_FAILURE
                              ))
    doctest.master.summarize(1)
    if result.failed == 0:
        print('ALL TESTS PASSED')
