import { computed } from 'vue'
import {
  BookOpen,
  Calendar,
  ClipboardList,
  GalleryVerticalEnd,
  GraduationCap,
  LayoutDashboard,
  Users,
  Settings2,
  PieChart,
  Award,
  Bell,
  MessageSquare,
  DollarSign,
  UserCheck,
  BookMarked,
  CalendarDays,
  FolderOpen,
  Activity,
} from 'lucide-vue-next'

export type UserRole = 'Admin' | 'Teacher' | 'Student'

export function useSidebarData(userRole: UserRole) {
  const sidebarData = computed(() => {
    const baseUser = {
      name: 'John Doe',
      email: 'user@example.com',
      avatar: '/avatars/default.jpg',
    }

    switch (userRole) {
      case 'Admin':
        return {
          user: baseUser,
          teams: [
            {
              name: 'UCV Admin Portal',
              logo: GalleryVerticalEnd,
              plan: 'Administrator',
            },
          ],
          navMain: [
            {
              title: 'Dashboard',
              url: '/admin/dashboard',
              icon: LayoutDashboard,
              isActive: true,
              items: [
                { title: 'Overview', url: '/admin/dashboard' },
                { title: 'Analytics', url: '/admin/analytics' },
              ],
            },
            {
              title: 'User Management',
              url: '#',
              icon: Users,
              items: [
                { title: 'Teachers', url: '/admin/teachers' },
                { title: 'Students', url: '/admin/students' },
                { title: 'Roles & Permissions', url: '/admin/roles' },
              ],
            },
            {
              title: 'Academic',
              url: '#',
              icon: BookOpen,
              items: [
                { title: 'Sections', url: '/admin/sections' },
                { title: 'Subjects', url: '/admin/subjects' },
                { title: 'School Years', url: '/admin/school-years' },
                { title: 'Schedules', url: '/admin/schedules' },
              ],
            },
            {
              title: 'Enrollment',
              url: '#',
              icon: UserCheck,
              items: [
                { title: 'Manage Enrollment', url: '/admin/enrollments' },
                { title: 'Enrollment History', url: '/admin/enrollments/history' },
              ],
            },
            {
              title: 'Announcements & Events',
              url: '#',
              icon: Bell,
              items: [
                { title: 'Announcements', url: '/admin/announcements' },
                { title: 'Events Calendar', url: '/admin/events' },
              ],
            },
            {
              title: 'Reports',
              url: '#',
              icon: PieChart,
              items: [
                { title: 'Grade Reports', url: '/admin/reports/grades' },
                { title: 'Attendance Reports', url: '/admin/reports/attendance' },
                { title: 'Payment Reports', url: '/admin/reports/payments' },
                { title: 'Activity Logs', url: '/admin/reports/logs' },
              ],
            },
            {
              title: 'Settings',
              url: '#',
              icon: Settings2,
              items: [
                { title: 'General', url: '/admin/settings/general' },
                { title: 'System', url: '/admin/settings/system' },
              ],
            },
          ],
          projects: [
            { name: 'System Logs', url: '/admin/logs', icon: Activity },
            { name: 'File Manager', url: '/admin/files', icon: FolderOpen },
          ],
        }

      case 'Teacher':
        return {
          user: baseUser,
          teams: [
            {
              name: 'UCV Teacher Portal',
              logo: GraduationCap,
              plan: 'Educator',
            },
          ],
          navMain: [
            {
              title: 'Dashboard',
              url: '/teacher/dashboard',
              icon: LayoutDashboard,
              isActive: true,
              items: [
                { title: 'Overview', url: '/teacher/dashboard' },
              ],
            },
            {
              title: 'My Classes',
              url: '#',
              icon: BookOpen,
              items: [
                { title: 'Subjects', url: '/teacher/subjects' },
                { title: 'Class Schedules', url: '/teacher/schedules' },
                { title: 'Advisory Section', url: '/teacher/advisory' },
              ],
            },
            {
              title: 'Students',
              url: '#',
              icon: Users,
              items: [
                { title: 'All Students', url: '/teacher/students' },
                { title: 'Attendance', url: '/teacher/attendance' },
                { title: 'Disciplinary Records', url: '/teacher/disciplinary' },
              ],
            },
            {
              title: 'Grades',
              url: '#',
              icon: Award,
              items: [
                { title: 'Input Grades', url: '/teacher/grades/input' },
                { title: 'View Grades', url: '/teacher/grades' },
                { title: 'Academic Honors', url: '/teacher/honors' },
              ],
            },
            {
              title: 'Assignments',
              url: '#',
              icon: ClipboardList,
              items: [
                { title: 'Create Assignment', url: '/teacher/assignments/new' },
                { title: 'View All', url: '/teacher/assignments' },
                { title: 'Submissions', url: '/teacher/assignments/submissions' },
              ],
            },
            {
              title: 'Learning Materials',
              url: '#',
              icon: BookMarked,
              items: [
                { title: 'Upload Materials', url: '/teacher/materials/upload' },
                { title: 'My Materials', url: '/teacher/materials' },
              ],
            },
            {
              title: 'Consultations',
              url: '#',
              icon: CalendarDays,
              items: [
                { title: 'Schedule', url: '/teacher/consultations' },
                { title: 'History', url: '/teacher/consultations/history' },
              ],
            },
            {
              title: 'Messages',
              url: '/teacher/messages',
              icon: MessageSquare,
              items: [
                { title: 'Messages', url: '/teacher/messages' },

              ],
            },
          ],
        }

      case 'Student':
        return {
          user: baseUser,
          teams: [
            {
              name: 'UCV Student Portal',
              logo: BookOpen,
              plan: 'Student',
            },
          ],
          navMain: [
            {
              title: 'Dashboard',
              url: '/student/dashboard',
              icon: LayoutDashboard,
              isActive: true,
              items: [
                { title: 'Overview', url: '/student/dashboard' },
              ],
            },
            {
              title: 'My Courses',
              url: '#',
              icon: BookOpen,
              items: [
                { title: 'Enrolled Subjects', url: '/student/subjects' },
                { title: 'Class Schedule', url: '/student/schedule' },
              ],
            },
            {
              title: 'Assignments',
              url: '#',
              icon: ClipboardList,
              items: [
                { title: 'Pending', url: '/student/assignments/pending' },
                { title: 'Submitted', url: '/student/assignments/submitted' },
                { title: 'Graded', url: '/student/assignments/graded' },
              ],
            },
            {
              title: 'Grades',
              url: '#',
              icon: Award,
              items: [
                { title: 'Current Grades', url: '/student/grades' },
                { title: 'Grade Report', url: '/student/grades/report' },
                { title: 'Academic Honors', url: '/student/honors' },
              ],
            },
            {
              title: 'Attendance',
              url: '#',
              icon: UserCheck,
              items: [
                { title: 'My Attendance', url: '/student/attendance' },
                { title: 'Attendance Summary', url: '/student/attendance/summary' },
              ],
            },
            {
              title: 'Learning Materials',
              url: '/student/materials',
              icon: BookMarked,
            },
            {
              title: 'Payments',
              url: '#',
              icon: DollarSign,
              items: [
                { title: 'View Payments', url: '/student/payments' },
                { title: 'Payment History', url: '/student/payments/history' },
              ],
            },
            {
              title: 'Consultations',
              url: '#',
              icon: CalendarDays,
              items: [
                { title: 'Request Consultation', url: '/student/consultations/request' },
                { title: 'My Consultations', url: '/student/consultations' },
              ],
            },
            {
              title: 'Messages',
              url: '/student/messages',
              icon: MessageSquare,
            },
            {
              title: 'Settings',
              url: '#',
              icon: Settings2,
              items: [
                { title: 'Profile', url: '/student/settings/profile' },
                { title: 'Preferences', url: '/student/settings/preferences' },
              ],
            },
          ],
          projects: [
            { name: 'Calendar', url: '/student/calendar', icon: Calendar },
            { name: 'Announcements', url: '/student/announcements', icon: Bell },
            { name: 'Events', url: '/student/events', icon: CalendarDays },
            { name: 'Clubs', url: '/student/clubs', icon: Users },
          ],
        }

      default:
        return {
          user: baseUser,
          teams: [],
          navMain: [],
          projects: [],
        }
    }
  })

  return { sidebarData }
}