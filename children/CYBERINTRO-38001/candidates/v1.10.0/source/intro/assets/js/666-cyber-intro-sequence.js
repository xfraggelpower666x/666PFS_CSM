/*
666 / LYVRA reusable intro controller
No redirect and no navigation are performed.
Completion only advances to the next local template stage and dispatches an event.
*/
(function () {
  'use strict';

  const root = document.querySelector('.lyvra-cyber-sequence');
  if (!root) return;

  const duration = Math.max(800, Number(root.dataset.introDuration || 4200));
  const transitionDuration = Math.max(300, Number(root.dataset.transitionDuration || 1100));
  const bar = root.querySelector('.lyvra-intro-bar');
  const percent = root.querySelector('.lyvra-intro-percent');
  const track = root.querySelector('.lyvra-intro-track');
  const status = root.querySelector('.lyvra-intro-status');
  const phaseLabel = root.querySelector('.lyvra-intro-phase-label');
  const steps = [...root.querySelectorAll('.lyvra-intro-step')];

  const phases = [
    { at: 0,  status: 'INITIALIZING INTERFACE',   label: 'CONNECTING PROJECT SIGNAL', step: 0 },
    { at: 24, status: 'AUTHENTICATING MODULES',   label: 'VERIFYING LOCAL COMPONENTS', step: 1 },
    { at: 52, status: 'SYNCHRONIZING PROTOCOLS',  label: 'PREPARING CYBER INTERFACE', step: 2 },
    { at: 82, status: 'INTRO SEQUENCE ARMED',     label: 'PROJECT INTERFACE READY', step: 3 },
    { at: 98, status: 'SEQUENCE COMPLETE',        label: 'PROJECT INTERFACE ONLINE', step: 3 }
  ];

  let start = 0;
  let raf = 0;
  let lastPhase = -1;
  let finished = false;

  function setPhase(progress) {
    let current = phases[0];
    for (const phase of phases) if (progress >= phase.at) current = phase;
    const phaseIndex = phases.indexOf(current);
    if (phaseIndex === lastPhase) return;
    lastPhase = phaseIndex;
    status.textContent = current.status;
    phaseLabel.textContent = current.label;
    steps.forEach((step, index) => {
      step.classList.toggle('done', index < current.step);
      step.classList.toggle('active', index === current.step);
    });
  }

  function complete() {
    if (finished) return;
    finished = true;
    if (raf) cancelAnimationFrame(raf);
    bar.style.width = '100%';
    percent.textContent = '100%';
    track.setAttribute('aria-valuenow', '100');
    status.textContent = 'SEQUENCE COMPLETE';
    phaseLabel.textContent = 'PROJECT INTERFACE ONLINE';
    steps.forEach(step => { step.classList.remove('active'); step.classList.add('done'); });
    root.classList.add('phase2-armed');
    root.classList.add('is-transitioning');
    root.dispatchEvent(new CustomEvent('lyvra:intro-transition-start', { bubbles: true }));
    window.dispatchEvent(new CustomEvent('lyvra:intro-transition-start', { detail: { root } }));

    window.setTimeout(() => {
      root.classList.add('intro-complete');
      root.classList.remove('is-transitioning');
      root.dispatchEvent(new CustomEvent('lyvra:intro-complete', { bubbles: true }));
      window.dispatchEvent(new CustomEvent('lyvra:intro-complete', { detail: { root } }));
    }, transitionDuration);
  }

  function tick(now) {
    if (!start) start = now;
    const elapsed = now - start;
    const progress = Math.min(100, Math.round((elapsed / duration) * 100));
    bar.style.width = progress + '%';
    percent.textContent = progress + '%';
    track.setAttribute('aria-valuenow', String(progress));
    setPhase(progress);
    if (elapsed < duration) raf = requestAnimationFrame(tick);
    else complete();
  }

  window.LyvraCyberIntro = {
    complete,
    skip: complete,
    reset() {
      if (raf) cancelAnimationFrame(raf);
      finished = false;
      start = 0;
      lastPhase = -1;
      root.classList.remove('intro-complete', 'is-transitioning', 'phase2-armed', 'system-online-sequence', 'system-started');
      window.dispatchEvent(new CustomEvent('lyvra:intro-reset', { detail: { root } }));
      bar.style.width = '0%';
      percent.textContent = '0%';
      track.setAttribute('aria-valuenow', '0');
      steps.forEach((step, index) => {
        step.classList.toggle('active', index === 0);
        step.classList.remove('done');
      });
      raf = requestAnimationFrame(tick);
    }
  };

  raf = requestAnimationFrame(tick);
})();
