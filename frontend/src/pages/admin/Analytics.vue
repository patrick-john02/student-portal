<script lang="ts">
export const description = "Analytics dashboard with charts and metrics"
export const iframeHeight = "800px"
export const containerClass = "w-full h-full"
</script>

<script setup lang="ts">
import AppSidebar from "@/components/sidebars/AppSidebar.vue"
import {
  Breadcrumb,
  BreadcrumbItem,
  BreadcrumbLink,
  BreadcrumbList,
  BreadcrumbPage,
  BreadcrumbSeparator,
} from "@/components/ui/breadcrumb"
import { Separator } from "@/components/ui/separator"
import {
  SidebarInset,
  SidebarProvider,
  SidebarTrigger,
} from "@/components/ui/sidebar"
import {
  Card,
  CardContent,
  CardDescription,
  CardHeader,
  CardTitle,
} from "@/components/ui/card"
import { Button } from "@/components/ui/button"
import {
  Select,
  SelectContent,
  SelectItem,
  SelectTrigger,
  SelectValue,
} from "@/components/ui/select"
import { Users, GraduationCap, BookOpen, TrendingUp, TrendingDown, Calendar } from "lucide-vue-next"

const userRole = 'Admin'
</script>

<template>
  <SidebarProvider>
    <AppSidebar :user-role="userRole" />
    <SidebarInset>
      <header class="flex h-16 shrink-0 items-center gap-2 transition-[width,height] ease-linear group-has-data-[collapsible=icon]/sidebar-wrapper:h-12">
        <div class="flex items-center gap-2 px-4">
          <SidebarTrigger class="-ml-1" />
          <Separator orientation="vertical" class="mr-2 h-4" />
          <Breadcrumb>
            <BreadcrumbList>
              <BreadcrumbItem class="hidden md:block">
                <BreadcrumbLink href="/admin/dashboard">
                  Admin
                </BreadcrumbLink>
              </BreadcrumbItem>
              <BreadcrumbSeparator class="hidden md:block" />
              <BreadcrumbItem>
                <BreadcrumbPage>Analytics</BreadcrumbPage>
              </BreadcrumbItem>
            </BreadcrumbList>
          </Breadcrumb>
        </div>
        <div class="ml-auto flex items-center gap-2 px-4">
          <Select default-value="2024">
            <SelectTrigger class="w-[180px]">
              <SelectValue placeholder="Select Year" />
            </SelectTrigger>
            <SelectContent>
              <SelectItem value="2024">2024-2025</SelectItem>
              <SelectItem value="2023">2023-2024</SelectItem>
              <SelectItem value="2022">2022-2023</SelectItem>
            </SelectContent>
          </Select>
          <Button variant="outline" size="sm">
            <Calendar class="mr-2 h-4 w-4" />
            Filter
          </Button>
        </div>
      </header>

      <div class="flex flex-1 flex-col gap-4 p-4 pt-0">
        <!-- Key Metrics -->
        <div class="grid gap-4 md:grid-cols-2 lg:grid-cols-4">
          <Card>
            <CardHeader class="flex flex-row items-center justify-between space-y-0 pb-2">
              <CardTitle class="text-sm font-medium">Total Students</CardTitle>
              <Users class="h-4 w-4 text-muted-foreground" />
            </CardHeader>
            <CardContent>
              <div class="text-2xl font-bold">1,284</div>
              <p class="text-xs text-muted-foreground flex items-center gap-1 mt-1">
                <TrendingUp class="h-3 w-3 text-green-500" />
                <span class="text-green-500">+12.5%</span> from last year
              </p>
            </CardContent>
          </Card>

          <Card>
            <CardHeader class="flex flex-row items-center justify-between space-y-0 pb-2">
              <CardTitle class="text-sm font-medium">Active Teachers</CardTitle>
              <GraduationCap class="h-4 w-4 text-muted-foreground" />
            </CardHeader>
            <CardContent>
              <div class="text-2xl font-bold">87</div>
              <p class="text-xs text-muted-foreground flex items-center gap-1 mt-1">
                <TrendingUp class="h-3 w-3 text-green-500" />
                <span class="text-green-500">+3</span> new this semester
              </p>
            </CardContent>
          </Card>

          <Card>
            <CardHeader class="flex flex-row items-center justify-between space-y-0 pb-2">
              <CardTitle class="text-sm font-medium">Total Subjects</CardTitle>
              <BookOpen class="h-4 w-4 text-muted-foreground" />
            </CardHeader>
            <CardContent>
              <div class="text-2xl font-bold">42</div>
              <p class="text-xs text-muted-foreground flex items-center gap-1 mt-1">
                <span class="text-muted-foreground">Across all strands</span>
              </p>
            </CardContent>
          </Card>

          <Card>
            <CardHeader class="flex flex-row items-center justify-between space-y-0 pb-2">
              <CardTitle class="text-sm font-medium">Avg. Attendance</CardTitle>
              <TrendingUp class="h-4 w-4 text-muted-foreground" />
            </CardHeader>
            <CardContent>
              <div class="text-2xl font-bold">94.2%</div>
              <p class="text-xs text-muted-foreground flex items-center gap-1 mt-1">
                <TrendingDown class="h-3 w-3 text-red-500" />
                <span class="text-red-500">-1.2%</span> from last month
              </p>
            </CardContent>
          </Card>
        </div>

        <!-- Charts Row -->
        <div class="grid gap-4 md:grid-cols-2 lg:grid-cols-7">
          <Card class="col-span-4">
            <CardHeader>
              <CardTitle>Enrollment Trends</CardTitle>
              <CardDescription>Student enrollment by strand over time</CardDescription>
            </CardHeader>
            <CardContent class="pl-2">
              <div class="h-[300px] flex items-center justify-center bg-muted/30 rounded-lg">
                <div class="text-center text-muted-foreground">
                  <TrendingUp class="h-12 w-12 mx-auto mb-2 opacity-50" />
                  <p class="text-sm">Line Chart: Enrollment by Strand</p>
                  <p class="text-xs mt-1">STEM, ABM, HUMSS, TVL, GAS</p>
                </div>
              </div>
            </CardContent>
          </Card>

          <Card class="col-span-3">
            <CardHeader>
              <CardTitle>Strand Distribution</CardTitle>
              <CardDescription>Current student distribution</CardDescription>
            </CardHeader>
            <CardContent>
              <div class="h-[300px] flex items-center justify-center bg-muted/30 rounded-lg">
                <div class="text-center text-muted-foreground">
                  <div class="h-12 w-12 rounded-full border-4 border-muted-foreground/50 mx-auto mb-2" />
                  <p class="text-sm">Pie Chart: Strand Distribution</p>
                  <p class="text-xs mt-1">STEM: 35%, ABM: 25%, etc.</p>
                </div>
              </div>
            </CardContent>
          </Card>
        </div>

        <!-- Statistics and Performance -->
        <div class="grid gap-4 md:grid-cols-2 lg:grid-cols-7">
          <Card class="col-span-3">
            <CardHeader>
              <CardTitle>Grade Performance</CardTitle>
              <CardDescription>Average grades by quarter</CardDescription>
            </CardHeader>
            <CardContent>
              <div class="h-[300px] flex items-center justify-center bg-muted/30 rounded-lg">
                <div class="text-center text-muted-foreground">
                  <div class="flex gap-2 justify-center mb-2">
                    <div class="h-12 w-8 bg-muted-foreground/30 rounded" />
                    <div class="h-12 w-8 bg-muted-foreground/40 rounded" />
                    <div class="h-12 w-8 bg-muted-foreground/50 rounded" />
                    <div class="h-12 w-8 bg-muted-foreground/60 rounded" />
                  </div>
                  <p class="text-sm">Bar Chart: Quarterly Performance</p>
                  <p class="text-xs mt-1">Q1: 85.2, Q2: 86.5, Q3: 87.1, Q4: 88.3</p>
                </div>
              </div>
            </CardContent>
          </Card>

          <Card class="col-span-4">
            <CardHeader>
              <CardTitle>Attendance Overview</CardTitle>
              <CardDescription>Monthly attendance rates by grade level</CardDescription>
            </CardHeader>
            <CardContent>
              <div class="space-y-4">
                <div class="space-y-2">
                  <div class="flex items-center justify-between text-sm">
                    <span class="font-medium">Grade 11</span>
                    <span class="text-muted-foreground">95.3%</span>
                  </div>
                  <div class="h-2 bg-muted rounded-full overflow-hidden">
                    <div class="h-full bg-primary rounded-full" style="width: 95.3%" />
                  </div>
                </div>

                <div class="space-y-2">
                  <div class="flex items-center justify-between text-sm">
                    <span class="font-medium">Grade 12</span>
                    <span class="text-muted-foreground">93.1%</span>
                  </div>
                  <div class="h-2 bg-muted rounded-full overflow-hidden">
                    <div class="h-full bg-primary rounded-full" style="width: 93.1%" />
                  </div>
                </div>

                <div class="space-y-2">
                  <div class="flex items-center justify-between text-sm">
                    <span class="font-medium">STEM Strand</span>
                    <span class="text-muted-foreground">96.5%</span>
                  </div>
                  <div class="h-2 bg-muted rounded-full overflow-hidden">
                    <div class="h-full bg-primary rounded-full" style="width: 96.5%" />
                  </div>
                </div>

                <div class="space-y-2">
                  <div class="flex items-center justify-between text-sm">
                    <span class="font-medium">ABM Strand</span>
                    <span class="text-muted-foreground">94.8%</span>
                  </div>
                  <div class="h-2 bg-muted rounded-full overflow-hidden">
                    <div class="h-full bg-primary rounded-full" style="width: 94.8%" />
                  </div>
                </div>

                <div class="space-y-2">
                  <div class="flex items-center justify-between text-sm">
                    <span class="font-medium">HUMSS Strand</span>
                    <span class="text-muted-foreground">92.7%</span>
                  </div>
                  <div class="h-2 bg-muted rounded-full overflow-hidden">
                    <div class="h-full bg-primary rounded-full" style="width: 92.7%" />
                  </div>
                </div>
              </div>
            </CardContent>
          </Card>
        </div>

        <!-- Recent Activity -->
        <Card>
          <CardHeader>
            <CardTitle>Recent Activity Summary</CardTitle>
            <CardDescription>Latest updates and metrics across the system</CardDescription>
          </CardHeader>
          <CardContent>
            <div class="grid gap-4 md:grid-cols-3">
              <div class="space-y-1 p-4 rounded-lg border bg-card">
                <p class="text-sm font-medium">New Enrollments</p>
                <p class="text-2xl font-bold">24</p>
                <p class="text-xs text-muted-foreground">This week</p>
              </div>
              <div class="space-y-1 p-4 rounded-lg border bg-card">
                <p class="text-sm font-medium">Pending Assignments</p>
                <p class="text-2xl font-bold">156</p>
                <p class="text-xs text-muted-foreground">Across all subjects</p>
              </div>
              <div class="space-y-1 p-4 rounded-lg border bg-card">
                <p class="text-sm font-medium">Payment Collection</p>
                <p class="text-2xl font-bold">87.3%</p>
                <p class="text-xs text-muted-foreground">This semester</p>
              </div>
            </div>
          </CardContent>
        </Card>
      </div>
    </SidebarInset>
  </SidebarProvider>
</template>