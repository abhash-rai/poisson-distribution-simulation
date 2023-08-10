# poisson-distribution-simulation

<div align="center">
    <img src="https://github.com/AbhashChamlingRai/poisson-distribution-simulation/assets/106548397/54de9410-2a77-4f87-819f-eb1d426b1446" alt="simulation_run">
</div>

<br>

# Prerequisites

- You must have `Python 3` installed on your system.
- You must have `Git` installed on your system.

<br>

# Installation

1. Clone the repository (In terminal):

   ```
   git clone https://github.com/AbhashChamlingRai/poisson-distribution-simulation.git
   ```

2. Navigate to the directory requirements.txt file is located.

   ```
   cd <path_to_requirements.txt>
   ```

3. Install the required dependencies:

   ```
   pip install -r requirements.txt
   ```

   <br>

# Usage

## Running the script:

```
python poisson.py [START_event] [END_event] [TARGET_event] [lambda_START_val] [lambda_END_val] [lambda_TARGET_val] <discrete_event_steps> <lambda_steps>
```

`* Arguments enclosed using [ ] are required, and < > are optional`

## Example:

```
python poisson.py 0 20 12 0 10 6.5       -> Setting six required args
python poisson.py 0 20 12 0 10 6.5 1     -> Setting six required args + <discrete_event_steps>
python poisson.py 0 20 12 0 10 6.5 1 0.5 -> Setting six required args + <discrete_event_steps> + <lambda_steps>
```

`* Note: (START_event < TARGET_event >= END_event) and (lambda_START_val < lambda_TARGET_val >= lambda_END_val)`

- These arguments require descrete (Int) values:

  [START_event] ,
  [END_event] ,
  [TARGET_event]

- While these arguments require quantative (Int/float) values:

  [lambda_START_val] ,
  [lambda_END_val] ,
  [lambda_TARGET_val] ,
  <discrete_event_steps> ,
  <lambda_steps>
