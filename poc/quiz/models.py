from django.db import models

class Program(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    def __str__(self):
        return str(self.name)

class Email(models.Model):
    id = models.AutoField(primary_key=True)
    email = models.CharField(max_length=200)
    def __str__(self):
        return str(self.email)

class Recommendation(models.Model):
    id = models.AutoField(primary_key=True)
    program = models.ForeignKey(Program, on_delete=models.CASCADE)
    code = models.CharField(max_length=200)
    def __str__(self):
        return str(self.program.name)

class Description(models.Model):
    id = models.AutoField(primary_key=True)
    program = models.ForeignKey(Recommendation, on_delete=models.CASCADE,default=None)
    description = models.TextField()
    hyperlink = models.TextField()
    def __str__(self):
        return str(self.program.program.name)

class CareerType(models.Model):
    id = models.AutoField(primary_key=True)
    option = models.CharField(max_length=200)
    def __str__(self):
        return str(self.option)

class CourseType(models.Model):
    id = models.AutoField(primary_key=True)
    option = models.CharField(max_length=200)
    def __str__(self):
        return str(self.option)

class Career(models.Model):
    id = models.AutoField(primary_key=True)
    program = models.ForeignKey(Recommendation, on_delete=models.CASCADE,default=None)
    career_type = models.ForeignKey(CareerType, on_delete=models.CASCADE)
    career = models.TextField()
    def __str__(self):
        return str(self.program.program.name)+" : "+str(self.career)

class Course(models.Model):
    id = models.AutoField(primary_key=True)
    program = models.ForeignKey(Recommendation, on_delete=models.CASCADE,default=None)
    course_type = models.ForeignKey(CourseType, on_delete=models.CASCADE)
    course = models.TextField()
    def __str__(self):
        return str(self.program.program.name)+" : "+str(self.course)

class Comparison(models.Model):
    id = models.AutoField(primary_key=True)
    program_1 = models.ForeignKey(Program, on_delete=models.CASCADE,related_name='program+')
    program_2 = models.ForeignKey(Program, on_delete=models.CASCADE,related_name='compared_to+')
    comparison = models.TextField()
    recommendation = models.ForeignKey(Recommendation, on_delete=models.CASCADE,default=None)
    def __str__(self):
        return str(self.program_1)+" vs. "+str(self.program_2)+" : "+str(self.comparison)

class Result(models.Model):
    id = models.AutoField(primary_key=True)
    time = models.CharField(max_length=200)
    problem_type = models.CharField(max_length=200)
    creative = models.CharField(max_length=200)
    outdoors = models.CharField(max_length=200)
    career = models.CharField(max_length=200)
    group_work = models.CharField(max_length=200)
    liked_courses = models.CharField(max_length=200)
    disliked_courses = models.CharField(max_length=200)
    programming = models.CharField(max_length=200)
    join_clubs = models.CharField(max_length=200)
    not_clubs = models.CharField(max_length=200)
    liked_projects = models.CharField(max_length=200)
    disliked_projects = models.CharField(max_length=200)
    tv_shows = models.CharField(max_length=200)
    alternate_degree = models.CharField(max_length=200)
    expensive_equipment = models.CharField(max_length=200)
    drawing = models.CharField(max_length=200)
    essay = models.CharField(max_length=200)
    architecture = models.CharField(max_length=200)
    automotive = models.CharField(max_length=200)
    business = models.CharField(max_length=200)
    construction = models.CharField(max_length=200)
    health = models.CharField(max_length=200)
    environment = models.CharField(max_length=200)
    manufacturing = models.CharField(max_length=200)
    technology = models.CharField(max_length=200)
    arch = models.CharField(max_length=200,default=None)
    arche = models.CharField(max_length=200,default=None)
    bmed = models.CharField(max_length=200,default=None)
    ce = models.CharField(max_length=200,default=None)
    cive = models.CharField(max_length=200,default=None)
    chem = models.CharField(max_length=200,default=None)
    env = models.CharField(max_length=200,default=None)
    elec = models.CharField(max_length=200,default=None)
    geo = models.CharField(max_length=200,default=None)
    mech = models.CharField(max_length=200,default=None)
    msci = models.CharField(max_length=200,default=None)
    nano = models.CharField(max_length=200,default=None)
    syde = models.CharField(max_length=200,default=None)
    swe = models.CharField(max_length=200,default=None)
    tron = models.CharField(max_length=200,default=None)

    def __str__(self):
        return_value = (
                        str(self.problem_type) + " , " +
                        str(self.creative) + " , " +
                        str(self.outdoors) + " , " +
                        str(self.career) + " , " +
                        str(self.group_work) + " , " +
                        str(self.liked_courses) + " , " +
                        str(self.disliked_courses) + " , " +
                        str(self.programming) + " , " +
                        str(self.join_clubs) + " , " +
                        str(self.not_clubs) + " , " +
                        str(self.liked_projects) + " , " +
                        str(self.disliked_projects) + " , " +
                        str(self.tv_shows) + " , " +
                        str(self.alternate_degree) + " , " +
                        str(self.expensive_equipment) + " , " +
                        str(self.drawing) + " , " +
                        str(self.essay) + " , " +
                        str(self.architecture) + " , " +
                        str(self.automotive) + " , " +
                        str(self.business) + " , " +
                        str(self.construction) + " , " +
                        str(self.health) + " , " +
                        str(self.environment) + " , " +
                        str(self.manufacturing) + " , " +
                        str(self.technology) + " , " +
                        str(self.arch) + " , " +
                        str(self.arche) + " , " +
                        str(self.bmed) + " , " +
                        str(self.ce) + " , " +
                        str(self.cive) + " , " +
                        str(self.chem) + " , " +
                        str(self.env) + " , " +
                        str(self.elec) + " , " +
                        str(self.geo) + " , " +
                        str(self.mech) + " , " +
                        str(self.msci) + " , " +
                        str(self.nano) + " , " +
                        str(self.syde) + " , " +
                        str(self.swe) + " , " +
                        str(self.tron)
                        )
        return return_value
