# Interactive Learning Rules

This file defines shared rules for interactive learning aids used in FE, GK, and DS study articles.

Use this rule together with the content rules for each section:

- FE: `docs/agent/fe-content-rules.md`
- GK: `docs/agent/gk-content-rules.md`
- DS: `docs/agent/ds-content-rules.md`

The goal is not to add animation or JavaScript for decoration. The goal is to make concepts easier to understand by letting learners see, compare, or manipulate the behavior that the article explains.

## Core Principle

Whenever creating a new article or making a substantial update to an existing article, explicitly consider whether an interactive or visual learning aid would materially improve beginner understanding.

An interactive aid is optional. Do not add one unless it clearly improves learning.

The required step is the evaluation, not the implementation.

The decision order is:

1. Can the concept be understood well from text alone?
2. Would a static HTML/CSS/SVG diagram be enough?
3. Would changing a value, state, order, or condition make the concept significantly easier to understand?

Use the lightest solution that achieves the learning goal.

## When To Propose An Interactive Aid

Consider an interactive aid when at least one of the following applies:

- a process changes step by step;
- changing a numeric parameter changes the result;
- comparing two or more methods helps reveal the difference;
- two representations must be mapped to each other, such as a matrix and a graph;
- a condition changes the processing result;
- a formula is hard to understand without seeing concrete values change;
- beginners are likely to struggle to imagine the process mentally;
- showing why a result changes is more useful than only showing the final answer.

Typical useful patterns include:

### Step-by-step pattern

Useful for topics such as:

- binary search;
- sorting;
- stack / queue operations;
- branching;
- iterative algorithms.

Let the learner advance one step at a time and show what changed.

### Parameter-change pattern

Useful for topics such as:

- activation functions;
- probabilities and expected values;
- averages and thresholds;
- evaluation metrics;
- simple statistical relationships.

Use sliders or small controls only when changing the value reveals the concept.

### Comparison pattern

Useful for topics such as:

- Max Pooling vs Average Pooling;
- linear search vs binary search;
- ReLU vs Sigmoid vs tanh;
- mean vs median;
- model or metric selection.

Use controls that let the learner switch between alternatives while keeping the comparison context stable.

### Mapping pattern

Useful for topics such as:

- adjacency matrix and graph;
- confusion matrix and derived metrics;
- neural-network layers and their roles;
- data structures and their visual representations.

When possible, changing one representation should visibly update the corresponding part of the other.

### Judgment pattern

Useful for topics such as:

- correlation vs causation;
- choosing an evaluation metric;
- choosing a model or method;
- identifying which condition changes the correct interpretation.

The interaction should reinforce the article's decision rule, not turn into a quiz for its own sake.

## Proposal Format

When an interactive aid would be useful but is not yet implemented, mention it briefly in the article creation or update proposal.

State these three points:

- what the learner would operate;
- what would visibly change;
- what concept or exam judgment the interaction would clarify.

Example:

> Binary search is a good candidate for an interactive aid: the learner can press a "next comparison" button, watch the discarded half fade out, and understand that the search range is reduced by half after each comparison.

If an interactive aid would not add meaningful learning value, say so briefly when that judgment matters. Do not force a proposal.

## Implementation Rules

- Prefer plain HTML, CSS, JavaScript, and inline SVG that work directly on GitHub Pages.
- Avoid external JavaScript libraries unless there is a clear learning or maintenance benefit.
- Prefer HTML/CSS/SVG over image files when the same explanation can be produced clearly without images.
- Keep JavaScript and CSS in reusable section-specific visualizer files whenever practical.
- Reuse and extend existing visualizer assets before creating new files.
- Do not place large JavaScript blocks directly in article Markdown unless there is a strong reason.
- Keep the interaction lightweight and fast on mobile devices.
- Make buttons and controls easy to use on smartphones.
- The article must remain understandable when JavaScript is unavailable.
- Do not make critical definitions, conclusions, or exam rules available only through interaction.
- Keep visible text short and beginner-friendly.
- Add a short instruction such as `見るポイント：...` so the learner knows what to observe.
- Keep the interaction simpler than the concept it explains.

## Learning Design

A good interactive aid should usually follow this flow:

```text
operate
↓
see what changes
↓
connect the change to the meaning
```

Do not display too many controls, states, or explanations at once.

Prefer one main learning objective per interactive block.

Avoid decorative motion. Animation should only be used when it helps the learner follow a state change or relationship.

## Section-Specific Priorities

### FE

Prioritize interactions that make processing steps, algorithms, data structures, comparisons, and state changes concrete.

Especially useful for:

- Subject B pseudocode tracing;
- search and sort algorithms;
- stacks, queues, trees, and graphs;
- conditions, loops, and variable changes;
- calculation processes where the order of operations matters.

The interaction should help the learner answer: `What changes next, and why?`

### GK

Prioritize interactions that clarify the role, behavior, or distinction of AI / machine-learning concepts and help eliminate incorrect answer choices.

Especially useful for:

- activation functions;
- pooling and convolution;
- thresholds and output interpretation;
- model architecture roles;
- evaluation metrics;
- differences between similar methods.

The interaction should help the learner answer: `Which feature belongs to which concept?`

### DS

Prioritize interactions that improve interpretation of data, statistics, analysis results, and practical decision-making.

Especially useful for:

- mean / median and distributions;
- correlation and causation;
- confusion matrices and metrics;
- thresholds;
- sampling and statistical intuition;
- choosing an analysis method.

The interaction should help the learner answer: `How should this result be interpreted?`

## Shared Teaching Interaction Standard

Use this sequence when predicting the next state genuinely improves learning:

1. **Predict:** Ask one concrete question before revealing the next state.
2. **Operate:** Provide a clearly named action such as 「次へ」 or 「取り出す」.
3. **Observe:** Show the changed state and briefly identify what changed.
4. **Judge:** Connect the result to the article's exam distinction or practical interpretation.

Prediction is optional, not a required quiz for every article. A static diagram or direct manipulation may teach the concept better. Do not block the normal demonstration when a learner skips prediction.

### Explain outputs before asking learners to interpret them

Before an interactive block displays metrics, abbreviations, scores, or calculated values that beginners may not recognize:

1. Introduce each output in plain Japanese: **what it measures**, **how it is calculated or derived**, and **why its change matters**.
2. Prefer a compact table or a few short sentences directly **before** the interactive block. Link to existing detailed articles for deeper explanations rather than repeating full lessons.
3. Give one focused observation prompt, such as 「FPを増やすとPrecisionはどう変わる？」, that connects an input to the meaning of an output.
4. Keep output labels consistent between the introductory explanation and the live results. Japanese terms can accompany English metric names.
5. Distinguish a demonstration that changes one count while holding others fixed from a comparison of predictions on the same fixed dataset. Do not imply that both are the same experiment.

Do not add an introductory table mechanically when the outputs are already familiar or clearly explained nearby. The learner should understand **what a displayed number means** before being asked to learn from its change.

### State and explanation

- Clearly distinguish **changed**, **currently selected/compared**, and **confirmed/fixed** states when those distinctions matter. Never label a changed position as a comparison unless the trace actually records comparisons.
- Describe the result in short Japanese text as well as with visual styling. Color alone must not carry meaning.
- Explain the scope of simplified traces: representative steps are not necessarily every comparison, assignment, or swap.
- Keep the learner's input, the displayed state, and the explanation synchronized after next, back, reset, mode changes, and boundary conditions.
- Use deterministic examples where possible, and show the initial state and final state clearly.

### Controls, accessibility, and fallbacks

- Label each input and button by its action; use semantic HTML controls and visible keyboard focus.
- Make interactive state changes understandable to screen-reader users, without excessive announcements.
- Support narrow screens and touch targets without requiring hover, precise dragging, or horizontal scrolling for the main operation.
- Provide a short static explanation or worked example when JavaScript is disabled.
- Avoid adding duplicate UI or shared-JavaScript behavior that interferes with other articles.

### Verification before merging

For every new or modified interaction, record what was actually checked and what remains unverified:

1. Initial state, normal operation, final state, reset, and mode switching if applicable.
2. Empty/full or other relevant boundary conditions; correct prediction and incorrect prediction when a quiz exists.
3. Agreement between numeric values, highlighted positions, explanatory text, and the article's exam rule.
4. Smartphone layout, keyboard operation, readable contrast, and JavaScript-disabled fallback.
5. Regression impact on other pages using the same CSS/JavaScript assets.
6. GitHub Pages build and deployed page when available. Never equate a successful commit with a successful deployment.

### Exam-specific outcome

- **FE:** The learner can trace what changes next and explain why.
- **GK:** The learner can distinguish the role or behavior of similar AI concepts and reject misleading choices.
- **DS:** The learner can interpret a result and explain how changed assumptions or values affect it.
- **SG:** The learner can choose an appropriate security or workplace response and explain the decision condition. Use the SG article rules when adapting an aid.

## When Not To Add One

Do not add an interactive aid when:

- the article is already clear from text alone;
- a static diagram communicates the idea just as well;
- the interaction would be mainly decorative;
- the controls are more complicated than the concept;
- the interaction would require knowledge beyond the target exam level;
- the mobile experience would be poor;
- the explanation of the interaction would become longer than the concept itself;
- the implementation would duplicate an existing visualizer without adding learning value.

## Maintenance And Consistency

When adding a new interaction:

- check whether a similar component already exists in `assets/js/*-visualizer.js` or `assets/css/*-visualizer.css`;
- extend existing patterns and class naming where practical;
- keep section-specific styles visually consistent with existing FE / GK / DS interactive aids;
- avoid introducing a new interaction style for every article;
- confirm that the page remains readable in both desktop and smartphone layouts;
- after implementation, confirm that the GitHub Pages build succeeds when possible.

## Final Self-Check

For a new article or substantial article update, confirm that:

- interactive / visual learning value was considered;
- the lightest useful format was chosen: text, static diagram, or interaction;
- an interactive proposal was made when changing values, states, order, or conditions would materially improve understanding;
- the interaction, if added, has one clear learning objective;
- the interaction supports the article's exam judgment or practical interpretation;
- the article still makes sense without JavaScript;
- the controls are usable on mobile;
- the interaction is not merely decorative.
