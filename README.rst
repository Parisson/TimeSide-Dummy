==============================================
TimeSide : open web audio processing framework
==============================================

Template for developing new TimeSide plugins packages
=====================================================

.. image:: https://travis-ci.org/Parisson/TimeSide-Dummy.svg?branch=master
    :target: https://travis-ci.org/Parisson/TimeSide-Dummy


TimeSide-Dummy is a template for developping new plugins for `TimeSide <https://github.com/Parisson/TimeSide>`_.

TimeSide is a set of python components enabling low and high level audio analysis, imaging, transcoding and streaming. Its high-level API is designed to enable complex processing on large datasets of audio and video assets of any format. Its simple plug-in architecture can be adapted to various use cases.

TimeSide also includes a smart interactive HTML5 player which provides various streaming playback functions, formats selectors, fancy audio visualizations, segmentation and semantic labelling synchronized with audio events. It is embeddable in any web application.


TimeSide is developped by `Parisson <http://parisson.com>`_.


Related projects
=================

* `Telemeta <http://telemeta.org>`__ : open web audio platform
* `Sound archives <http://archives.crem-cnrs.fr/>`_ of the CNRS, CREM and the "Musée de l'Homme" in Paris, France.
 
How-To
======

Thanks to Docker, TimeSide is now fully available for every platform as a docker image ready to work. The image includes all the necessary applications, modules and volumes to start your project in a few seconds.

Just install, `Docker engine <https://docs.docker.com/installation/>`_ and `docker-compose <https://docs.docker.com/compose/install/>`_.

To develop and test the TimeSide Dummy plugins package inside an ipython console, just run ::

    docker-compose run app ipython


The plugins reside in the `timeside/plugins/dummy/` directory.

You can also run your code in the wonderful `Jupyter Notebook <http://jupyter.org/>`_ which gives you a web interface to run your own code and share the results with your collaborators::

    docker-compose up

and then browse  http://localhost:8888 to acces the Jupyter notebook interface.

.. note ::
    On MacOS or Windows, you will need to ask the IP of the virtual machine to docker-machine::

        docker-machine ip timeside

    If it gives you for example 192.168.59.103, you should be able to browse the notebook at http://192.168.59.103:8888/

    
.. warning :: Running a Jupyter notebook server with this setup in a non-secured network is not safe. See `Running a notebook server <http://jupyter-notebook.readthedocs.org/en/latest/public_server.html/>`_ for a documented solution to this security problem.


.. note :: If you need to user TimeSide outside a docker image please refer to the rules of the Dockerfile which is based on a Debian stable system. But we do not provide any kind of free support in this usercase anymore (the dependency list is now huge). To get commercial support in more various usecases, please reach the Parisson dev team.


