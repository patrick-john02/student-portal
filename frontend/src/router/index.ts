import { createRouter, createWebHistory, type RouteRecordRaw } from "vue-router";

// Lazy-loaded components
const Login = () => import("@/pages/Login.vue");

// Admin Pages
const AdminDashboard = () => import("@/pages/admin/Dashboard.vue");
const AdminAnalytics = () => import("@/pages/admin/Analytics.vue");
const AdminTeachers = () => import("@/pages/admin/Teachers.vue");
const AdminStudents = () => import("@/pages/admin/Students.vue");
const AdminRoles = () => import("@/pages/admin/Roles.vue");
const AdminSections = () => import("@/pages/admin/Sections.vue");
const AdminSubjects = () => import("@/pages/admin/Subjects.vue");
const AdminSchoolYears = () => import("@/pages/admin/SchoolYears.vue");
const AdminSchedules = () => import("@/pages/admin/Schedules.vue");
const AdminEnrollments = () => import("@/pages/admin/Enrollments.vue");
const AdminEnrollmentHistory = () => import("@/pages/admin/EnrollmentHistory.vue");
const AdminAnnouncements = () => import("@/pages/admin/Announcements.vue");
const AdminEvents = () => import("@/pages/admin/Events.vue");
const AdminGradeReports = () => import("@/pages/admin/reports/Grades.vue");
const AdminAttendanceReports = () => import("@/pages/admin/reports/Attendance.vue");
// const AdminPaymentReports = () => import("@/pages/admin/reports/Payments.vue");
const AdminActivityLogs = () => import("@/pages/admin/reports/Logs.vue");
const AdminSettingsGeneral = () => import("@/pages/admin/settings/General.vue");
const AdminSettingsSystem = () => import("@/pages/admin/settings/System.vue");
const AdminLogs = () => import("@/pages/admin/Logs.vue");
const AdminFiles = () => import("@/pages/admin/Files.vue");

// Teacher Pages
const TeacherDashboard = () => import("@/pages/teacher/Dashboard.vue");
const TeacherSubjects = () => import("@/pages/teacher/Subjects.vue");
const TeacherSchedules = () => import("@/pages/teacher/Schedules.vue");
const TeacherAdvisory = () => import("@/pages/teacher/Advisory.vue");
const TeacherStudents = () => import("@/pages/teacher/Students.vue");
const TeacherAttendance = () => import("@/pages/teacher/Attendance.vue");
const TeacherDisciplinary = () => import("@/pages/teacher/Disciplinary.vue");
const TeacherGradeInput = () => import("@/pages/teacher/grades/Input.vue");
const TeacherGrades = () => import("@/pages/teacher/Grades.vue");
const TeacherHonors = () => import("@/pages/teacher/Honors.vue");
const TeacherAssignmentNew = () => import("@/pages/teacher/assignments/New.vue");
const TeacherAssignments = () => import("@/pages/teacher/Assignments.vue");
const TeacherSubmissions = () => import("@/pages/teacher/assignments/Submissions.vue");
const TeacherMaterialsUpload = () => import("@/pages/teacher/materials/Upload.vue");
const TeacherMaterials = () => import("@/pages/teacher/Materials.vue");
const TeacherConsultations = () => import("@/pages/teacher/Consultations.vue");
const TeacherConsultationHistory = () => import("@/pages/teacher/consultations/History.vue");
const TeacherMessages = () => import("@/pages/teacher/Messages.vue");
const TeacherSettingsProfile = () => import("@/pages/teacher/settings/Profile.vue");
const TeacherSettingsPreferences = () => import("@/pages/teacher/settings/Preferences.vue");

// Student Pages
const StudentDashboard = () => import("@/pages/student/Dashboard.vue");
const StudentSubjects = () => import("@/pages/student/Subjects.vue");
const StudentSchedule = () => import("@/pages/student/Schedule.vue");
const StudentAssignmentsPending = () => import("@/pages/student/assignments/Pending.vue");
const StudentAssignmentsSubmitted = () => import("@/pages/student/assignments/Submitted.vue");
const StudentAssignmentsGraded = () => import("@/pages/student/assignments/Graded.vue");
const StudentGrades = () => import("@/pages/student/Grades.vue");
const StudentGradeReport = () => import("@/pages/student/grades/Report.vue");
const StudentHonors = () => import("@/pages/student/Honors.vue");
const StudentAttendance = () => import("@/pages/student/Attendance.vue");
// const StudentAttendanceSummary = () => import("@/pages/student/attendance/Summary.vue");
// const StudentMaterials = () => import("@/pages/student/Materials.vue");
// const StudentPayments = () => import("@/pages/student/Payments.vue");
// const StudentPaymentHistory = () => import("@/pages/student/payments/History.vue");
// const StudentConsultationRequest = () => import("@/pages/student/consultations/Request.vue");
// const StudentConsultations = () => import("@/pages/student/Consultations.vue");
// const StudentMessages = () => import("@/pages/student/Messages.vue");
// const StudentSettingsProfile = () => import("@/pages/student/settings/Profile.vue");
// const StudentSettingsPreferences = () => import("@/pages/student/settings/Preferences.vue");
// const StudentCalendar = () => import("@/pages/student/Calendar.vue");
// const StudentAnnouncements = () => import("@/pages/student/Announcements.vue");
// const StudentEvents = () => import("@/pages/student/Events.vue");
// const StudentClubs = () => import("@/pages/student/Clubs.vue");

const routes: RouteRecordRaw[] = [
  {
    path: "/",
    redirect: "/login",
  },
  {
    path: "/login",
    name: "Login",
    component: Login,
    meta: { requiresAuth: false },
  },

  // ==================== ADMIN ROUTES ====================
  {
    path: "/admin",
    redirect: "/admin/dashboard",
    meta: { requiresAuth: true, role: "Admin" },
  },
  {
    path: "/admin/dashboard",
    name: "AdminDashboard",
    component: AdminDashboard,
    // meta: { requiresAuth: true, role: "Admin" },
  },
  {
    path: "/admin/analytics",
    name: "AdminAnalytics",
    component: AdminAnalytics,
    // meta: { requiresAuth: true, role: "Admin" },
  },
  {
    path: "/admin/teachers",
    name: "AdminTeachers",
    component: AdminTeachers,
    // meta: { requiresAuth: true, role: "Admin" },
  },
  {
    path: "/admin/students",
    name: "AdminStudents",
    component: AdminStudents,
    // meta: { requiresAuth: true, role: "Admin" },
  },
  {
    path: "/admin/roles",
    name: "AdminRoles",
    component: AdminRoles,
    // meta: { requiresAuth: true, role: "Admin" },
  },
  {
    path: "/admin/sections",
    name: "AdminSections",
    component: AdminSections,
    // meta: { requiresAuth: true, role: "Admin" },
  },
  {
    path: "/admin/subjects",
    name: "AdminSubjects",
    component: AdminSubjects,
    // meta: { requiresAuth: true, role: "Admin" },
  },
  {
    path: "/admin/school-years",
    name: "AdminSchoolYears",
    component: AdminSchoolYears,
    // meta: { requiresAuth: true, role: "Admin" },
  },
  {
    path: "/admin/schedules",
    name: "AdminSchedules",
    component: AdminSchedules,
    // meta: { requiresAuth: true, role: "Admin" },
  },
  {
    path: "/admin/enrollments",
    name: "AdminEnrollments",
    component: AdminEnrollments,
    // meta: { requiresAuth: true, role: "Admin" },
  },
  {
    path: "/admin/enrollments/history",
    name: "AdminEnrollmentHistory",
    component: AdminEnrollmentHistory,
    // meta: { requiresAuth: true, role: "Admin" },
  },
  {
    path: "/admin/announcements",
    name: "AdminAnnouncements",
    component: AdminAnnouncements,
    // meta: { requiresAuth: true, role: "Admin" },
  },
  {
    path: "/admin/events",
    name: "AdminEvents",
    component: AdminEvents,
    // meta: { requiresAuth: true, role: "Admin" },
  },
  {
    path: "/admin/reports/grades",
    name: "AdminGradeReports",
    component: AdminGradeReports,
    // meta: { requiresAuth: true, role: "Admin" },
  },
  {
    path: "/admin/reports/attendance",
    name: "AdminAttendanceReports",
    component: AdminAttendanceReports,
    // meta: { requiresAuth: true, role: "Admin" },
  },
  // {
  //   path: "/admin/reports/payments",
  //   name: "AdminPaymentReports",
  //   component: AdminPaymentReports,
  //   meta: { requiresAuth: true, role: "Admin" },
  // },
  {
    path: "/admin/reports/logs",
    name: "AdminActivityLogs",
    component: AdminActivityLogs,
    // meta: { requiresAuth: true, role: "Admin" },
  },
  {
    path: "/admin/settings/general",
    name: "AdminSettingsGeneral",
    component: AdminSettingsGeneral,
    // meta: { requiresAuth: true, role: "Admin" },
  },
  {
    path: "/admin/settings/system",
    name: "AdminSettingsSystem",
    component: AdminSettingsSystem,
    // meta: { requiresAuth: true, role: "Admin" },
  },
  {
    path: "/admin/logs",
    name: "AdminLogs",
    component: AdminLogs,
    // meta: { requiresAuth: true, role: "Admin" },
  },
  {
    path: "/admin/files",
    name: "AdminFiles",
    component: AdminFiles,
    // meta: { requiresAuth: true, role: "Admin" },
  },

  // // ==================== TEACHER ROUTES ====================
  {
    path: "/teacher",
    redirect: "/teacher/dashboard",
    // meta: { requiresAuth: true, role: "Teacher" },
  },
  {
    path: "/teacher/dashboard",
    name: "TeacherDashboard",
    component: TeacherDashboard,
    // meta: { requiresAuth: true, role: "Teacher" },
  },
  {
    path: "/teacher/subjects",
    name: "TeacherSubjects",
    component: TeacherSubjects,
    // meta: { requiresAuth: true, role: "Teacher" },
  },
  {
    path: "/teacher/schedules",
    name: "TeacherSchedules",
    component: TeacherSchedules,
    // meta: { requiresAuth: true, role: "Teacher" },
  },
  {
    path: "/teacher/advisory",
    name: "TeacherAdvisory",
    component: TeacherAdvisory,
    // meta: { requiresAuth: true, role: "Teacher" },
  },
  {
    path: "/teacher/students",
    name: "TeacherStudents",
    component: TeacherStudents,
    // meta: { requiresAuth: true, role: "Teacher" },
  },
  {
    path: "/teacher/attendance",
    name: "TeacherAttendance",
    component: TeacherAttendance,
    // meta: { requiresAuth: true, role: "Teacher" },
  },
  {
    path: "/teacher/disciplinary",
    name: "TeacherDisciplinary",
    component: TeacherDisciplinary,
    // meta: { requiresAuth: true, role: "Teacher" },
  },
  {
    path: "/teacher/grades/input",
    name: "TeacherGradeInput",
    component: TeacherGradeInput,
    // meta: { requiresAuth: true, role: "Teacher" },
  },
  {
    path: "/teacher/grades",
    name: "TeacherGrades",
    component: TeacherGrades,
    // meta: { requiresAuth: true, role: "Teacher" },
  },
  {
    path: "/teacher/honors",
    name: "TeacherHonors",
    component: TeacherHonors,
    // meta: { requiresAuth: true, role: "Teacher" },
  },
  {
    path: "/teacher/assignments/new",
    name: "TeacherAssignmentNew",
    component: TeacherAssignmentNew,
    // meta: { requiresAuth: true, role: "Teacher" },
  },
  {
    path: "/teacher/assignments",
    name: "TeacherAssignments",
    component: TeacherAssignments,
    // meta: { requiresAuth: true, role: "Teacher" },
  },
  {
    path: "/teacher/assignments/submissions",
    name: "TeacherSubmissions",
    component: TeacherSubmissions,
    // meta: { requiresAuth: true, role: "Teacher" },
  },
  {
    path: "/teacher/materials/upload",
    name: "TeacherMaterialsUpload",
    component: TeacherMaterialsUpload,
    // meta: { requiresAuth: true, role: "Teacher" },
  },
  {
    path: "/teacher/materials",
    name: "TeacherMaterials",
    component: TeacherMaterials,
    // meta: { requiresAuth: true, role: "Teacher" },
  },
  {
    path: "/teacher/consultations",
    name: "TeacherConsultations",
    component: TeacherConsultations,
    // meta: { requiresAuth: true, role: "Teacher" },
  },
  {
    path: "/teacher/consultations/history",
    name: "TeacherConsultationHistory",
    component: TeacherConsultationHistory,
    // meta: { requiresAuth: true, role: "Teacher" },
  },
  {
    path: "/teacher/messages",
    name: "TeacherMessages",
    component: TeacherMessages,
    // meta: { requiresAuth: true, role: "Teacher" },
  },
  {
    path: "/teacher/settings/profile",
    name: "TeacherSettingsProfile",
    component: TeacherSettingsProfile,
    // meta: { requiresAuth: true, role: "Teacher" },
  },
  {
    path: "/teacher/settings/preferences",
    name: "TeacherSettingsPreferences",
    component: TeacherSettingsPreferences,
    // meta: { requiresAuth: true, role: "Teacher" },
  },

  // // ==================== STUDENT ROUTES ====================
  {
    path: "/student",
    redirect: "/student/dashboard",
    // meta: { requiresAuth: true, role: "Student" },
  },
  {
    path: "/student/dashboard",
    name: "StudentDashboard",
    component: StudentDashboard,
    // meta: { requiresAuth: true, role: "Student" },
  },
  {
    path: "/student/subjects",
    name: "StudentSubjects",
    component: StudentSubjects,
    // meta: { requiresAuth: true, role: "Student" },
  },
  {
    path: "/student/schedule",
    name: "StudentSchedule",
    component: StudentSchedule,
    // meta: { requiresAuth: true, role: "Student" },
  },
  {
    path: "/student/assignments/pending",
    name: "StudentAssignmentsPending",
    component: StudentAssignmentsPending,
    // meta: { requiresAuth: true, role: "Student" },
  },
  {
    path: "/student/assignments/submitted",
    name: "StudentAssignmentsSubmitted",
    component: StudentAssignmentsSubmitted,
    // meta: { requiresAuth: true, role: "Student" },
  },
  {
    path: "/student/assignments/graded",
    name: "StudentAssignmentsGraded",
    component: StudentAssignmentsGraded,
    // meta: { requiresAuth: true, role: "Student" },
  },
  {
    path: "/student/grades",
    name: "StudentGrades",
    component: StudentGrades,
    // meta: { requiresAuth: true, role: "Student" },
  },
  {
    path: "/student/grades/report",
    name: "StudentGradeReport",
    component: StudentGradeReport,
    // meta: { requiresAuth: true, role: "Student" },
  },
  {
    path: "/student/honors",
    name: "StudentHonors",
    component: StudentHonors,
    // meta: { requiresAuth: true, role: "Student" },
  },
  {
    path: "/student/attendance",
    name: "StudentAttendance",
    component: StudentAttendance,
    // meta: { requiresAuth: true, role: "Student" },
  },
  // {
  //   path: "/student/attendance/summary",
  //   name: "StudentAttendanceSummary",
  //   component: StudentAttendanceSummary,
  //   meta: { requiresAuth: true, role: "Student" },
  // },
  // {
  //   path: "/student/materials",
  //   name: "StudentMaterials",
  //   component: StudentMaterials,
  //   meta: { requiresAuth: true, role: "Student" },
  // },
  // {
  //   path: "/student/payments",
  //   name: "StudentPayments",
  //   component: StudentPayments,
  //   meta: { requiresAuth: true, role: "Student" },
  // },
  // {
  //   path: "/student/payments/history",
  //   name: "StudentPaymentHistory",
  //   component: StudentPaymentHistory,
  //   meta: { requiresAuth: true, role: "Student" },
  // },
  // {
  //   path: "/student/consultations/request",
  //   name: "StudentConsultationRequest",
  //   component: StudentConsultationRequest,
  //   meta: { requiresAuth: true, role: "Student" },
  // },
  // {
  //   path: "/student/consultations",
  //   name: "StudentConsultations",
  //   component: StudentConsultations,
  //   meta: { requiresAuth: true, role: "Student" },
  // },
  // {
  //   path: "/student/messages",
  //   name: "StudentMessages",
  //   component: StudentMessages,
  //   meta: { requiresAuth: true, role: "Student" },
  // },
  // {
  //   path: "/student/settings/profile",
  //   name: "StudentSettingsProfile",
  //   component: StudentSettingsProfile,
  //   meta: { requiresAuth: true, role: "Student" },
  // },
  // {
  //   path: "/student/settings/preferences",
  //   name: "StudentSettingsPreferences",
  //   component: StudentSettingsPreferences,
  //   meta: { requiresAuth: true, role: "Student" },
  // },
  // {
  //   path: "/student/calendar",
  //   name: "StudentCalendar",
  //   component: StudentCalendar,
  //   meta: { requiresAuth: true, role: "Student" },
  // },
  // {
  //   path: "/student/announcements",
  //   name: "StudentAnnouncements",
  //   component: StudentAnnouncements,
  //   meta: { requiresAuth: true, role: "Student" },
  // },
  // {
  //   path: "/student/events",
  //   name: "StudentEvents",
  //   component: StudentEvents,
  //   meta: { requiresAuth: true, role: "Student" },
  // },
  // {
  //   path: "/student/clubs",
  //   name: "StudentClubs",
  //   component: StudentClubs,
  //   meta: { requiresAuth: true, role: "Student" },
  // },

  // ==================== 404 ROUTE ====================
  {
    path: "/:pathMatch(.*)*",
    redirect: "/login",
  },
];

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes,
});

// Navigation guard for authentication and role-based access
router.beforeEach((to, from, next) => {
  // Get user authentication state and role from your auth store/service
  // Example: const { isAuthenticated, userRole } = useAuthStore()
  const isAuthenticated = false; // Replace with actual auth check
  const userRole = null; // Replace with actual role: 'Admin' | 'Teacher' | 'Student'

  if (to.meta.requiresAuth && !isAuthenticated) {
    // Redirect to login if route requires auth and user is not authenticated
    next("/login");
  } else if (to.meta.role && to.meta.role !== userRole) {
    // Redirect to appropriate dashboard if user role doesn't match
    if (userRole === "Admin") next("/admin/dashboard");
    else if (userRole === "Teacher") next("/teacher/dashboard");
    else if (userRole === "Student") next("/student/dashboard");
    else next("/login");
  } else {
    next();
  }
});

export default router;