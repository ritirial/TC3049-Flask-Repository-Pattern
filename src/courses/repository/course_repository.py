import abc

from courses.model.course_model import Course


class CourseRepository(abc.ABC):

    @abc.abstractmethod
    def add(self, user: Course) -> Course:
        raise NotImplementedError


    @abc.abstractmethod
    def get(self, id: int) -> Course:
        raise NotImplementedError


class LocalCourseRepository(CourseRepository):

    def __init__(self):
        self.courses = []


    def add(self, name: str, description: str) -> Course:
        
        # find if name was already used
        name_used = None
        for item in self.courses:
            if item.name == name:
                name_used = item
                break

        # End function if name is not available
        if name_used is not None:
            return None
        
        # Generate object and append to DB list
        course = Course(
            id = len(self.courses) + 1,
            name = name,
            description = description
        )

        self.courses.append(course)
        return course


    def get(self, id: int) -> Course:
        item_found = None

        for course in self.courses:

            if course.id == id:
                item_found = course
                break

        return item_found