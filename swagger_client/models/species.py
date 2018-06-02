# coding: utf-8

"""
    Studio Ghibli API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class Species(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'id': 'str',
        'name': 'str',
        'classification': 'str',
        'eye_color': 'str',
        'hair_color': 'str',
        'people': 'str',
        'films': 'str',
        'url': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'classification': 'classification',
        'eye_color': 'eye_color',
        'hair_color': 'hair_color',
        'people': 'people',
        'films': 'films',
        'url': 'url'
    }

    def __init__(self, id=None, name=None, classification=None, eye_color=None, hair_color=None, people=None, films=None, url=None):  # noqa: E501
        """Species - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._name = None
        self._classification = None
        self._eye_color = None
        self._hair_color = None
        self._people = None
        self._films = None
        self._url = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if classification is not None:
            self.classification = classification
        if eye_color is not None:
            self.eye_color = eye_color
        if hair_color is not None:
            self.hair_color = hair_color
        if people is not None:
            self.people = people
        if films is not None:
            self.films = films
        if url is not None:
            self.url = url

    @property
    def id(self):
        """Gets the id of this Species.  # noqa: E501

        Unique identifier representing a specific species  # noqa: E501

        :return: The id of this Species.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Species.

        Unique identifier representing a specific species  # noqa: E501

        :param id: The id of this Species.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this Species.  # noqa: E501

        Name of the species  # noqa: E501

        :return: The name of this Species.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Species.

        Name of the species  # noqa: E501

        :param name: The name of this Species.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def classification(self):
        """Gets the classification of this Species.  # noqa: E501

        Classification of the species  # noqa: E501

        :return: The classification of this Species.  # noqa: E501
        :rtype: str
        """
        return self._classification

    @classification.setter
    def classification(self, classification):
        """Sets the classification of this Species.

        Classification of the species  # noqa: E501

        :param classification: The classification of this Species.  # noqa: E501
        :type: str
        """

        self._classification = classification

    @property
    def eye_color(self):
        """Gets the eye_color of this Species.  # noqa: E501

        Eye color of the species  # noqa: E501

        :return: The eye_color of this Species.  # noqa: E501
        :rtype: str
        """
        return self._eye_color

    @eye_color.setter
    def eye_color(self, eye_color):
        """Sets the eye_color of this Species.

        Eye color of the species  # noqa: E501

        :param eye_color: The eye_color of this Species.  # noqa: E501
        :type: str
        """

        self._eye_color = eye_color

    @property
    def hair_color(self):
        """Gets the hair_color of this Species.  # noqa: E501

        Hair color of the species  # noqa: E501

        :return: The hair_color of this Species.  # noqa: E501
        :rtype: str
        """
        return self._hair_color

    @hair_color.setter
    def hair_color(self, hair_color):
        """Sets the hair_color of this Species.

        Hair color of the species  # noqa: E501

        :param hair_color: The hair_color of this Species.  # noqa: E501
        :type: str
        """

        self._hair_color = hair_color

    @property
    def people(self):
        """Gets the people of this Species.  # noqa: E501

        People belonging to the species  # noqa: E501

        :return: The people of this Species.  # noqa: E501
        :rtype: str
        """
        return self._people

    @people.setter
    def people(self, people):
        """Sets the people of this Species.

        People belonging to the species  # noqa: E501

        :param people: The people of this Species.  # noqa: E501
        :type: str
        """

        self._people = people

    @property
    def films(self):
        """Gets the films of this Species.  # noqa: E501

        Array of films the species appears in  # noqa: E501

        :return: The films of this Species.  # noqa: E501
        :rtype: str
        """
        return self._films

    @films.setter
    def films(self, films):
        """Sets the films of this Species.

        Array of films the species appears in  # noqa: E501

        :param films: The films of this Species.  # noqa: E501
        :type: str
        """

        self._films = films

    @property
    def url(self):
        """Gets the url of this Species.  # noqa: E501

        Unique url of the species  # noqa: E501

        :return: The url of this Species.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this Species.

        Unique url of the species  # noqa: E501

        :param url: The url of this Species.  # noqa: E501
        :type: str
        """

        self._url = url

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, Species):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
