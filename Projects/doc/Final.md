<div align="center">
	<img src="https://crunchbase-production-res.cloudinary.com/image/upload/c_pad,h_140,w_140/v1465765206/j2ocvfzcvgk8dxjkilvv.png"/>
	<h1>
		<p>Instituto Superior de Engenharia de Lisboa</p>
		<p>Artificial Intelligence for Autonomous Systems</p>
	</h1>
	<p>André Fonseca</p>
	<p>A39758@alunos.isel.pt</p><br/>
	<p>Professor Paulo Vieira</p>
	<p>pjvieira@deetc.isel.pt<p/><br/>
	<p>June 2017<p/>
</div>

<br/><br/>

# Table of contents
1. [Introduction](#introduction)
2. [Artificial intelligence overview](#artificial-intelligence-overview)
3. [Intelligent agents](#intelligent-agents)
4. [Search strategies](#search-strategies)
5. [Markov decision process]()
6. [Reinforcement learning]()
7. [Project #1](#first-project)
8. [Project #2](#second-project)
9. [Project #3](#third-project)
10. [Conclusions](#conclusions)

----------

<div align="center">
	<img src="https://readwrite.com/wp-content/uploads/iStock-586712790-e1496714940902.jpg"/>
</div>

> *"We tend to overestimate the effect of a technology in the short run and underestimate the effect in the long run."* - Roy Amara
<br/>

<br/>

# Introduction
This final report aims to describe and explain all the subjects studied in the Artificial Intelligence for Autonomous Systems class. During the semester three projects were developed with the provided architectural system models.

The first project simulates the interactions between an agent and an environment which the agent belongs to. When the simulation starts the gatekeeper goes into patrol mode. In case of hearing a noise the gatekeeper inspects the area, searching for the noise’s origin. If there is no longer any noise, then he continues to patrol. At any time the gatekeeper may encounter an enemy and in that case he must protect the area and warn the foe to retreat. In this situation, if the enemy backs off, he will remain inspecting the area for any source of noise. In case the enemy persists, the gatekeeper will have to defend himself and fight the threat. In combat situation two actions may occur. The gatekeeper can be victorious and defeat the enemy and, then, he goes back to patrol; or in case of defeat the simulation is restarted. The interaction, at any level, is made by text inputs and outputs.

The second project implement an autonomous resolution system of the 8 puzzle problem. The initial problem presents two puzzle configurations to be solved, but the main objective is to develop a solution that is able to solve any kind of puzzle configuration or, even further, any kind of problem that fits the developed problem model. The 8 puzzle problem is a smaller version of the slightly better known 15 puzzle game. The puzzle consists of an area divided into a grid of 3 by 3. On each grid square is a tile, except for one square which remains empty. Thus, there are eight tiles. A tile that is next to the empty grid square can be moved into the empty space, leaving the previous position empty in turn. Tiles are numbered, 1 to 8, so that each tile can be uniquely identified. The puzzle is solved using multiple search algorithms such as bread-first search, depth-first search and other variants.

The last project (...)

Before going into the projects analysis and resolutions (...)

# Artificial intelligence overview
AI has always intrigued people, from TV shows, movies and marketing using robots with pseudo-intelligence. It is the perfect topic to craft thrillers, adventures and dramas, just like the well known Terminator movie or the brilliant Westworld TV show.

The most basic definition of intelligence is: *the ability to learn and solve problems.*[^1] This is regardless of being human intelligence or machine intelligence. So artificial intelligence could be described as the *intelligence exhibited by machines or software.*[^2] To be more specific it's the study and design of intelligent agents - a system that perceives it's environment and takes actions that maximizes its chances of success.[^3]

## Definition throughout history
As history goes on the definition of AI has changed and four approaches mastered their own definition.

### Thinking humanly
The cognitive approach in which machines are designed with minds, machines that think in the full and literal sense. It requires scientific theories of internal activities of the brain and how humans think.

### Acting humanly
Machines have to act and do things like humans. This was the definition purposed by Alan Turing in the well known Turing Test: where a computer passes the test if a human interrogator, after posing some written questions, cannot tell whether the written responses come from a person or a computer. The major components suggested by Alan Turing were: knowledge, reasoning, language understanding and learning.

### Thinking rationally
AI is made using math merged with logic. It uses some notations and rules of inference or derivations for thoughts to codify all knowledge in this representation and use it to derive new knowledge.

### Acting rationally
Intelligent systems are designed to act and to maximize their goal. The intelligent agents are expected to maximize the goal achievement giving the available information about the environment, the background knowledge, past experiences and other useful information.

This last approach is the one adopted in the study objectives of IASA class.

## Applications
AI is present in people's daily lives without their awareness. Some applications:

 - Speech recognition:  Used by virtual assistants like Google Now, Siri and Amazon Echo;
 - Hand writing recognition: Used by banks to recognize checks information;
 - Machine translation: To translate sentences from one language to another;
 - Robotics: Robots can be used in many fields such as robotics surgery, navigation etc;
 - Spam filters: Used by email clients to filter out spam emails. These filters can learn over time based on user actions and classification techniques;
 - Face recognition: Used to identify faces and people's emotions in photographs and videos;
 - Medical imaging: Used to analyze patient's exams and detect diseases;
 - Autonomous vehicles: Vehicles that can drive autonomously without the intervention of a human.

# Intelligent agents
* What is an agent
* Agent vs objects
* [^3]

An agent perceives its own environment and act upon that environment to achieve a certain task. An agent could be seen as a function `f` that goes from something that he perceives `P` to a set of actions `A`.

<div align="center">
	<img src="https://latex.codecogs.com/gif.latex?f:&space;P&space;\rightarrow&space;A" title="f: P \rightarrow A" />
</div>

Rational agents can be defined as agents that do the right thing and rationality is relative to how to act in order to maximize a performance measure - factor that describes how well the agent is doing when performing a certain task to reach a certain goal.

## Agent and environments

## Rationality
* Notions of intelligence, cognition and rationality
* Different types of rationality

## Environments

## Agent architecture
* BDI architecture
* http://transectscience.org/pdfs/vol1n1/1118_35.pdf
* http://www.pucrs.br/facin-prov/wp-content/uploads/sites/19/2016/03/tr008.pdf
* http://www.dca.fee.unicamp.br/~gudwin/courses/IA889/2014/IA889-05.pdf

## Types of agents
* Main types of agent architectures and how they they use the notions of intelligence, cognition and rationality.
* Internal representation of reactive and deliberation architectures.

### Simple reflex agents

### Model-based reflex agents

### Goal-based agents

### Utility-based agents

### Learning agents

# Search strategies
* https://github.com/shiffman/NOC-S17-2-Intelligence-Learning/tree/master/week1-graphs
* [^3]
* [^4]

## Uninformed search strategies

### Breadth-first search

### Uniform-cost search

### Depth-first search

### Iterative deepening search

### Comparing uninformed search strategies

## Informed search strategies
* Describe the heuristic function and define and use heuristic functions

### Greedy best-first search

### A* search

# Markov decision process

## Finding optimal policy

# Reinforcement learning
* Definition of RL

## SARSA algorithm

## Q-Learning algorithm

# First project
## Requirements engineering

## Design

## Implementation

## Verification and validation

# Second project
## Requirements engineering

## Design

## Implementation

## Verification and validation

# Third project
## Requirements engineering

## Design

## Implementation

## Verification and validation


# Conclusions
One of the great promises of AI is its potential to help us unearth new knowledge in complex domains. We’ve already seen exciting glimpses of this, when our algorithms found ways to dramatically improve energy use in data centres - as well as of course with our program AlphaGo.

UML:
https://softwareengineering.stackexchange.com/questions/305031/why-is-uml-not-used-in-most-free-software-e-g-on-linux
https://www.quora.com/Why-should-I-use-or-not-use-UML

Everyone uses AI:
The term artificial intelligence is thrown around a lot these days, but usually, when a startup says they’re applying AI to some problem, it just means they are using machine learning in varying degrees of sophistication. And there is a big difference. Not to say machine learning doesn’t have huge potential for automation and optimizing computer responses to various problems, but artificial intelligence is at a completely different level.
https://www.theatlantic.com/technology/archive/2017/03/what-is-artificial-intelligence/518547/

[^1]: Definition of intelligence, Merriam-Webster [&nearr;](https://www.merriam-webster.com/dictionary/intelligence)

[^2]: Definition of artificial intelligence, Wikipedia [&nearr;](https://en.wikipedia.org/wiki/Artificial_intelligence)

[^3]: S. Russell and P. Norvig. Artificial Intelligence: A Modern Approach, chapter 4. Prentice Hall, 2nd edition, 2003.

[^4]: Preparing for the future of artificial intelligence - Executive Office of the President National Science and Technology Council  Committee on Technology [&nearr;](https://obamawhitehouse.archives.gov/sites/default/files/whitehouse_files/microsites/ostp/NSTC/preparing_for_the_future_of_ai.pdf)

[^5]: Grokking Algorithms: An illustrated guide for programmers and other curious people

[^6]: Innovations of AlphaGo [&nearr;](https://deepmind.com/blog/innovations-alphago/)

[^7]: Deep Reinforcement Learning [&nearr;](https://deepmind.com/blog/deep-reinforcement-learning/)

[^8]: Understanding the hype vs reality around artificial intelligence [&nearr;](https://readwrite.com/2017/06/05/understanding-reality-artificial-intelligence-dl1/)

[^9]: In the AI age, "being smart" will mean something completely different [&nearr;](https://hbr.org/2017/06/in-the-ai-age-being-smart-will-mean-something-completely-different)

[^10]: 'Artificial intelligence' has become meaningless [&nearr;](https://www.theatlantic.com/technology/archive/2017/03/what-is-artificial-intelligence/518547/)

*[AI]: Artificial Intelligence

*[IASA]: Artificial Intelligence for Autonomous Systems
