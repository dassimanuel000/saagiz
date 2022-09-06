import decimal
import graphene
from graphene_django import DjangoObjectType
from .models import Project, Job

class ProjectType(DjangoObjectType):
    class Meta: 
        model = Project
        fields = ('id','title')

  
class JobType(DjangoObjectType):
    class Meta: 
        model = Job
        fields = (
            'id',
            'title',
            'author',
            'technologie',
            'description',
            'status',
            'date_created',
        )  

class Query(graphene.ObjectType):
    projects = graphene.List(ProjectType)
    jobs = graphene.List(JobType)

    def resolve_jobs(root, info, **kwargs):
        # Querying a list
        return Job.objects.all()

    def resolve_projects(root, info, **kwargs):
        # Querying a list
        return Project.objects.all()

class UpdateProject(graphene.Mutation):
    class Arguments:
        # Mutation to update a project 
        title = graphene.String(required=True)
        id = graphene.ID()


    project = graphene.Field(ProjectType)

    @classmethod
    def mutate(cls, root, info, title, id):
        project = Project.objects.get(pk=id)
        project.title = title
        project.save()
        
        return UpdateProject(project=project)

class CreateProject(graphene.Mutation):
    class Arguments:
        # Mutation to create a project
        title = graphene.String(required=True)

    # Class attributes define the response of the mutation
    project = graphene.Field(ProjectType)

    @classmethod
    def mutate(cls, root, info, title):
        project = Project()
        project.title = title
        project.save()
        
        return CreateProject(project=project)

class JobInput(graphene.InputObjectType):
    title = graphene.String()
    author = graphene.String()
    technologie = graphene.Int()
    description = graphene.String()
    status = graphene.String()

class CreateJob(graphene.Mutation):
    class Arguments:
        input = JobInput(required=True)

    job = graphene.Field(JobType)
    
    @classmethod
    def mutate(cls, root, info, input):
        job = Job()
        job.title = input.title
        job.author = input.author
        job.technologie = input.technologie
        job.description = input.description
        job.status = input.status
        job.save()
        return CreateJob(job=job)

class UpdateJob(graphene.Mutation):
    class Arguments:
        input = JobInput(required=True)
        id = graphene.ID()

    job = graphene.Field(JobType)
    
    @classmethod
    def mutate(cls, root, info, input, id):
        job = Project.objects.get(pk=id)
        job.name = input.name
        job.description = input.description
        job.technologie = input.technologie
        job.save()
        return UpdateJob(job=job)

class Mutation(graphene.ObjectType):
    update_project = UpdateProject.Field()
    create_project = CreateProject.Field()
    create_job = CreateJob.Field()
    update_job = UpdateJob.Field()

schema = graphene.Schema(query=Query, mutation=Mutation)