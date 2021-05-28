DATA = [
    {
        'name': 'Facundo',
        'age': 72,
        'organization': 'Platzi',
        'position': 'Technical Coach',
        'language': 'python',
    },
    {
        'name': 'Luisana',
        'age': 33,
        'organization': 'Globant',
        'position': 'UX Designer',
        'language': 'javascript',
    },
    {
        'name': 'Héctor',
        'age': 19,
        'organization': 'Platzi',
        'position': 'Associate',
        'language': 'ruby',
    },
    {
        'name': 'Gabriel',
        'age': 20,
        'organization': 'Platzi',
        'position': 'Associate',
        'language': 'javascript',
    },
    {
        'name': 'Isabella',
        'age': 30,
        'organization': 'Platzi',
        'position': 'QA Manager',
        'language': 'java',
    },
    {
        'name': 'Karo',
        'age': 23,
        'organization': 'Everis',
        'position': 'Backend Developer',
        'language': 'python',
    },
    {
        'name': 'Ariel',
        'age': 32,
        'organization': 'Rappi',
        'position': 'Support',
        'language': '',
    },
    {
        'name': 'Juan',
        'age': 17,
        'organization': '',
        'position': 'Student',
        'language': 'go',
    },
    {
        'name': 'Pablo',
        'age': 32,
        'organization': 'Master',
        'position': 'Human Resources Manager',
        'language': 'python',
    },
    {
        'name': 'Lorena',
        'age': 56,
        'organization': 'Python Organization',
        'position': 'Language Maker',
        'language': 'python',
    },
]
def run():
    # all_python_devs = [worker["name"] for worker in DATA if worker["language"] == "python"]
    # for worker in all_python_devs:
    #      print(worker)

   
#    adults = list(filter(lambda worker: worker ["age"] > 18, DATA))
#    adults = list(map(lambda worker: worker["name"], adults)) 
#    for worker in adults:
#        print(worker)

    # reto list comprenhension 
    # old_people = [worker["name"] for worker in DATA if worker["age"] >50]
    # for worker in old_people:
    #     print(worker)

    # reto list comprenhension 
    # adults = [workers["name"] for workers in DATA if workers["age"] > 18]
    # for workers in adults:
    #     print(workers)

    #Reto python high order functions
    # all_python_devs = list(filter(lambda workers: workers["language"] == "python", DATA))
    # all_python_devs = list(map(lambda workers: workers["name"], all_python_devs))
    # for workers in all_python_devs:
    #     print(workers)

    all_platzi_workers = list(filter(lambda workers: workers["organization"] == "Platzi", DATA))
    all_platzi_workers = list(map(lambda workers: workers["name"], all_platzi_workers))
    for workers in all_platzi_workers:
        print(workers)

if __name__ == '__main__':
    run()
