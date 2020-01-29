# Changing questions into column headers for readability
READ_HEADERS = {
                'What Engineering program are you in?':'program',
                'Are you happy with what your program provides you with (i.e. courses, job opportunities, projects, etc.)':'happy',
                'What kind of problems do you enjoy solving?':'problem_type',
                'Would you consider yourself as being creative?':'creative',
                'What industry can you see yourself working in, in the future? Select all that apply.':'industry',
                'How comfortable are you working in the outdoors?':'outdoors',
                'What can you see yourself doing in the future?':'career',
                'How do you feel about group work? ':'group_work',
                'What high school class did you enjoy the most?':'liked_courses',
                'What high school class did you enjoy the least?':'disliked_courses',
                'How do you feel about computer programming?':'programming',
                'What type of club would you consider joining?':'join_clubs',
                'What type of club would you NOT want to join?':'not_clubs',
                'What project would you want to be a part of? ':'liked_projects',
                'What project do you find the least interesting?':'disliked_projects',
                'If you could only watch one TV show for the rest of your life, what would it be?':'tv_shows',
                'If engineering didn’t exist, what would you consider studying?':'alternate_degree',
                'How do you feel about working with expensive equipment?':'expensive_equipment',
                'How would you describe your drawing abilities?':'drawing',
                'You have an assignment to write an essay about anything you want. How does that make you feel?':'essay',
                "What is your gender?  **We're asking this to discover any gender biases in our questions**":'gender'
                }

READ_PROGRAMS = {
                'Mechanical Engineering':'mech',
                'Biomedical Engineering':'bmed',
                'Software Engineering':'swe',
                'Computer Engineering':'ce',
                'Mechatronics Engineering':'tron',
                'Civil Engineering':'cive',
                'Chemical Engineering':'chem',
                'Systems Design Engineering':'syde',
                'Management Engineering':'msci',
                'Electrical Engineering':'elec',
                'Nanotechnology Engineering':'nano',
                'Geological Engineering':'geo',
                'Environmental Engineering':'env',
                'Architectural Engineering':'arch-e',
                'Architecture':'arch'
                }

READ_PROBLEMS = {
                'Problems that are well defined.':'defined',
                'Problems that require some investigation.':'investigate',
                'Problems with very limited information.':'discover'
                }

READ_CREATIVE = {
                'I am somewhat creative.':'somewhat_creative',
                'I am not creative.' : 'not_creative',
                'I am very creative.' : 'creative'
                }

READ_INDUSTRY = {
                'Architecture (i.e. Designing a building taller than the CN Tower)':'architecture',
                'Automotive (i.e. Designing a new autonomous car)':'automotive',
                'Business (i.e. Starting your own consulting company)':'business',
                'Construction (i.e. Building a smart city)':'construction',
                'Health (i.e. Creating technology for minimally invasive surgeries)':'health',
                'Environment (i.e. Producing energy in sustainable ways)':'environment',
                'Manufacturing (i.e. Optimization or automation of manufacturing processes)':'manufacturing',
                'Technology (i.e. Working with cloud based software)':'technology'
                }

READ_OUTDOORS = {
                'Working outside would be okay, but only for short periods of time.':'limited',
                'I would rather work inside.':'indoors',
                'I love the outdoors and wish I could work outside every day.':'outdoors'
                }

READ_CAREERS = {
                'Building things with moving parts.':'moving_parts',
                'Designing or building sensor based technology.':'sensors',
                'Programming apps.':'programming',
                'Optimizing processes.':'optimizing',
                "Improving the way we use the world's resources.":'resources',
                'Designing buildings.':'buildings',
                'Making discoveries at the molecular level.':'molecules'
                }

READ_GROUPWORK = {
                'I occasionally like working with others.':'occasionally',
                'I enjoy working with others.':'yes',
                'I do not like working as part of a team. I would rather work alone.':'no'
                 }

READ_COURSES = {
                'Autoshop':'autoshop',
                'Biology':'biology',
                'Business':'business',
                'Chemistry':'chemistry',
                'Computer Science':'computer_science',
                'Geography':'geography',
                'History':'history',
                'Language Arts':'language_arts',
                'Math':'math',
                'Physics':'physics',
                'Visual Arts':'visual_arts'
                }

READ_PROGRAMMING = {
                    "I can code but it's not my favourite thing to do.":'partial',
                    "I code, I enjoy it and I'm good at it.":'complete',
                    'I don’t code and I have no desire to learn.':'no',
                    "I don't code but I am interested in trying it.":'interested'
                    }

READ_CLUBS = {
            'Art or design club (i.e. Fashion for Change)':'art/design',
            'Autoshop club (i.e. Autonomoose Autonomous Car Club)':'autoshop',
            'Business club (i.e. UW Finance Association)':'business',
            'Consulting club (i.e. DECA)':'consulting',
            'Environment club (i.e. UW Energy Network)':'environment',
            'Robotics club (i.e. UW Robotics Team)':'robotics',
            'Hacker club (i.e. UW Hacks)':'hacker_club',
            'Student council (i.e. Engineering Society)':'student_council',
            }

READ_PROJECTS = {
                'Prototyping a musical instrument for children with a disability.':'prototyping_instrument',
                'Designing a water treatment system for Mars.':'mars_water_treatment',
                'Programming a robot that can make you dinner.':'robot',
                'Building the world’s most powerful supercomputer.':'supercomputer',
                'Designing an Olympic village.':'olympic_village',
                'Creating a battery from recycled material.':'battery',
                'Optimizing the Uber Pool routes.':'uber_pool'
                }

READ_TV = {
            'Big Bang Theory':'big_bang_theory',
            'Breaking Bad':'breaking_bad',
            'Grey’s Anatomy':'greys_anatomy',
            'House Hunters':'house_hunters',
            'Myth Busters':'myth_busters',
            'Planet Earth':'planet_earth',
            'Silicon Valley':'silicon_valley'
            }

READ_ALTERNATE_DEGREE = {
            'Applied Science':'applied_science',
            'Business':'business',
            'Computer Science':'cs',
            'Economics':'econ',
            'English Literature':'lit',
            'Environmental Studies':'env',
            'Finance':'fin',
            'Geography':'geo',
            'Graphic Design':'design',
            'Health Studies':'health',
            'Marketing':'marketing',
            'Math':'math',
            'Political Science':'poli_sci',
            'Psychology':'psych',
            'Visual Arts':'visual_arts'
            }

READ_EQUIPMENT = {
            'That sounds cool!':'yes',
            "Could be cool, but I don't really care about fancy equipment or how much it costs.":'maybe',
            "That scares me and I don't want to touch it.":'no'
            }

READ_DRAWING = {
            'I am not the best, but I am not the worst.':'partial',
            'I am not very good.':'bad',
            'Really good, I can draw just about anything.':'good'
            }

READ_ESSAY = {
            'Excited! I can share my theories with the world.':'yes',
            'Annoyed. I would much rather be given a topic with clear instructions.':'no',
            'A bit apprehensive. I get overwhelmed with so many options.':'partial'
            }

INDEX_PROGRAM = {
                'mech': 9,
                'bmed': 2,
                'swe': 12,
                'tron': 14,
                'cive': 5,
                'chem': 4,
                'syde': 13,
                'msci': 10,
                'ce': 3,
                'elec': 6,
                'nano': 11,
                'geo': 8,
                'env': 7,
                'arch-e': 1,
                'arch': 0
                }
INV_INDEX_PROGRAM= {
            9:'mech',
            2:'bmed',
            12:'swe',
            14:'tron',
            5:'cive',
            4:'chem',
            13:'syde',
            10:'msci',
            3:'ce',
            6:'elec',
            11:'nano',
            8:'geo',
            7:'env',
            1:'arch-e',
            0:'arch'
            }
