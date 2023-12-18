<!-- Improved compatibility of back to top link: See: https://github.com/othneildrew/Best-README-Template/pull/73 -->
<a name="readme-top"></a>
<!--
*** Thanks for checking out the Best-README-Template. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
*** or simply open an issue with the tag "enhancement".
*** Don't forget to give the project a star!
*** Thanks again! Now go create something AMAZING! :D
-->



<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->

[![Apache License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]



<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/tywilson5/CookLevin-VertexCover">
    <img src="Vertex_cover50.jpg" alt="Logo" width="80" height="80">
  </a>

<h3 align="center">CookLevin-VertexCover</h3>

  <p align="center">
    This program generates a random graph and then solves the vertex cover problem. 
    Using the graph, it creates a CNF formula and then uses the glucose solver to solve it.

    
    
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

![CookLevin-VertexCover Screen Shot][product-screenshot]

My final for CS373 explores a strategy for solving NP-complete problems via polynomial time reductions. We know by the Cook-Levin theorem that any problem with a polynomial time verifier can be reduced to SAT, so in this project I reduce Vertex Cover to SAT using CNF boolean statements. 

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started



### Prerequisites

This is an example of how to list things you need to use the software and how to install them.
* pip
  ```sh
  pip install python-sat
  ```


<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Usage
Simply initialize the graph with the number of vertices that you want to generate, then solve it.


20:

![CookLevin-VertexCover Screen Shot][product-screenshot]

50:

[![CookLevin-VertexCover Screen Shot][product-screenshot2]]

200:

[![CookLevin-VertexCover Screen Shot][product-screenshot3]]



<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- LICENSE -->
## License

Distributed under the Apache License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTACT -->
## Contact

Tyler Wilson - [@GitHub](https://github.com/tywilson5) - Tywilson@ursinus.edu

Project Link: [https://github.com/tywilson5/CookLevin-VertexCover](https://github.com/tywilson5/CookLevin-VertexCover)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

* [CS373 CookLevinForReal](https://github.com/ursinus-cs373-f2023/CookLevinForReal)
* [Glucose SAT solver](https://github.com/audemard/glucose)


<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/tywilson5/CookLevin-VertexCover.svg?style=for-the-badge
[contributors-url]: https://github.com/tywilson5/CookLevin-VertexCover/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/tywilson5/CookLevin-VertexCover.svg?style=for-the-badge
[forks-url]: https://github.com/tywilson5/CookLevin-VertexCover/network/members
[stars-shield]: https://img.shields.io/github/stars/tywilson5/CookLevin-VertexCover.svg?style=for-the-badge
[stars-url]: https://github.com/tywilson5/CookLevin-VertexCover/stargazers
[issues-shield]: https://img.shields.io/github/issues/tywilson5/CookLevin-VertexCover.svg?style=for-the-badge
[issues-url]: https://github.com/tywilson5/CookLevin-VertexCover/issues
[license-shield]: https://img.shields.io/github/license/tywilson5/CookLevin-VertexCover.svg?style=for-the-badge
[license-url]: https://github.com/tywilson5/CookLevin-VertexCover/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/linkedin_username
[product-screenshot]: Vertex_cover20.jpg
[product-screenshot2]: Vertex_cover50.jpg
[product-screenshot3]: Vertex_cover200.jpg
[Next.js]: https://img.shields.io/badge/next.js-000000?style=for-the-badge&logo=nextdotjs&logoColor=white
[Next-url]: https://nextjs.org/
[React.js]: https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB
[React-url]: https://reactjs.org/
[Vue.js]: https://img.shields.io/badge/Vue.js-35495E?style=for-the-badge&logo=vuedotjs&logoColor=4FC08D
[Vue-url]: https://vuejs.org/
[Angular.io]: https://img.shields.io/badge/Angular-DD0031?style=for-the-badge&logo=angular&logoColor=white
[Angular-url]: https://angular.io/
[Svelte.dev]: https://img.shields.io/badge/Svelte-4A4A55?style=for-the-badge&logo=svelte&logoColor=FF3E00
[Svelte-url]: https://svelte.dev/
[Laravel.com]: https://img.shields.io/badge/Laravel-FF2D20?style=for-the-badge&logo=laravel&logoColor=white
[Laravel-url]: https://laravel.com
[Bootstrap.com]: https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white
[Bootstrap-url]: https://getbootstrap.com
[JQuery.com]: https://img.shields.io/badge/jQuery-0769AD?style=for-the-badge&logo=jquery&logoColor=white
[JQuery-url]: https://jquery.com 