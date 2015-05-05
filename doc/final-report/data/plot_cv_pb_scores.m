#!/usr/bin/env octave -qf

figure('visible','off');

s = load('scores.txt');
s = s / 1e6;
plot(s(:,1), s(:,2), 'bo', 'MarkerSize', 12, 'MarkerFaceColor', 'auto');

grid on;

% title('RMSE / 10^6 ', 'FontSize', 16, 'FontWeight', 'bold', 'FontName', 'Helvetica');
xlabel('Cross-Validation', 'FontSize', 16, 'FontName', 'Helvetica');
ylabel('Public Board', 'FontSize', 16, 'FontName', 'Helvetica');

h = legend('RMSE');

set(h, 'FontSize', 16, 'FontName', 'Helvetica');

ylim([1.6 2.0])

set(gca, 'FontSize', 16, 'FontName', 'Helvetica');

print('-depsc', '../figs/cv_pb_scores.eps', '-S800,400');